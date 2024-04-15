from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
import requests
import csv

default_args = {
    "owner": "dzikri",
    "retries": 3,
    "retry_delay": timedelta(minutes=5),
}

# Fungsi untuk mendapatkan data dari API
def get_data_from_api(endpoint):
    response = requests.get(endpoint)
    return response.json()

# Fungsi untuk menulis data ke dalam file CSV
def write_to_csv(file_path, **kwargs):
    response_data = kwargs['ti'].xcom_pull(task_ids='get_data_from_api')
    with open(file_path, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=response_data[0].keys())
        writer.writeheader()
        writer.writerows(response_data)

# Fungsi untuk menulis data ke dalam file TXT
def write_to_txt(file_path, **kwargs):
    response_data = kwargs['ti'].xcom_pull(task_ids='get_data_from_api')
    with open(file_path, 'w') as txt_file:
        for item in response_data:
            txt_file.write(','.join(map(str, item.values())) + '\n')

# Fungsi untuk menampilkan pesan "done!"
def print_done():
    print("Done!")

# Konfigurasi DAG
with DAG(
    dag_id='prioritas_2',
    default_args=default_args,
    description="Mengambil data dari API dan menulis ke file CSV dan TXT",
    start_date=datetime(2024, 4, 12, 2),
    schedule_interval='@daily',
    catchup=False
) as dag:

    # Task untuk mendapatkan data dari API
    get_data_task = PythonOperator(
        task_id='get_data_from_api',
        python_callable=get_data_from_api,
        op_kwargs={'endpoint': 'https://fakestoreapi.com/products'},
        provide_context=True
    )

    # Task untuk menulis hasil dari response API ke dalam file CSV
    write_to_csv_task = PythonOperator(
        task_id='write_to_csv',
        python_callable=write_to_csv,
        op_kwargs={'file_path': 'dags/data/output/products.csv'},
        provide_context=True
    )

    # Task untuk menulis hasil dari response API ke dalam file TXT
    write_to_txt_task = PythonOperator(
        task_id='write_to_txt',
        python_callable=write_to_txt,
        op_kwargs={'file_path': 'dags/data/output/products.txt'},
        provide_context=True
    )

    # Task untuk menampilkan pesan "done!"
    print_done_task = BashOperator(
        task_id='print_done',
        bash_command='echo "done!"'
    )

# Aliran task
get_data_task >> [write_to_csv_task, write_to_txt_task] >> print_done_task
