from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
import pandas as pd
import requests

default_args = {
    'owner': 'dzikri',
    'depends_on_past': False,
    'start_date': days_ago(1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

dag = DAG(
    'data_cleaning_dag',
    default_args=default_args,
    description='A DAG to perform data cleaning',
    schedule_interval=None,
)

def get_data_from_api():
    url = 'https://gist.githubusercontent.com/nadirbslmh/b50406d5579e875e6435896c9ff6c80c/raw/cac8007653b6145e9ad0ec69b1e4fd6c1be718e7/transactions.json'
    response = requests.get(url)
    data = response.json()
    return data

def clean_and_save_data(**kwargs):
    ti = kwargs['ti']
    data = ti.xcom_pull(task_ids='get_data_from_api_task')
    
    cleaned_data = []
    for transaction in data:
        if 'transaction_status' in transaction and transaction['transaction_status'] == 'success':
            cleaned_transaction = {
                'transaction_id': transaction['transaction_id'],
                'customer_name': transaction['customer_name'],
                'phone_number': '+62' + transaction['phone_number'][1:],
                'transaction_amount': 'Rp {:,}'.format(transaction['transaction_amount']),
                'transaction_status': transaction['transaction_status']
            }
            cleaned_data.append(cleaned_transaction)
            print("Cleaned transaction:", cleaned_transaction)  
    
    cleaned_df = pd.DataFrame(cleaned_data)
    cleaned_df.to_csv('cleaned_data.csv', index=False) 
    print("Data cleaned and saved to CSV file.")

get_data_from_api_task = PythonOperator(
    task_id='get_data_from_api_task',
    python_callable=get_data_from_api,
    dag=dag,
)

clean_and_save_data_task = PythonOperator(
    task_id='clean_and_save_data_task',
    python_callable=clean_and_save_data,
    provide_context=True,
    dag=dag,
)

get_data_from_api_task >> clean_and_save_data_task
