from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
import seaborn as sns
import kaggle
import os

def download_dataset():
    kaggle.api.authenticate()
    kaggle.api.dataset_download_files("warcoder/earthquake-dataset", path="/tmp", unzip=True)

def transform_data(**kwargs):
    input_file = '/tmp/earthquake_1995-2023.csv'
    df = pd.read_csv(input_file)
    # Lakukan proses transformasi data di sini
    # Contoh: df = df.dropna()
    transformed_file = '/tmp/data_transformasi.csv'
    df.to_csv(transformed_file, index=False)
    return transformed_file

def export_to_excel(**kwargs):
    transformed_file = kwargs['ti'].xcom_pull(task_ids='transform_data')
    df = pd.read_csv(transformed_file)
    output_file = '/tmp/analysis_results.xlsx'
    df.to_excel(output_file, index=False)
    return output_file

def visualize_data(**kwargs):
    transformed_file = kwargs['ti'].xcom_pull(task_ids='transform_data')
    df = pd.read_csv(transformed_file)
    print(df.head())  # Cetak beberapa baris pertama DataFrame
    # Pastikan nama kolom yang digunakan sesuai dengan nama kolom yang ada dalam DataFrame
    sns.scatterplot(x='title', y='magnitude', hue='date_time', data=df, palette='viridis')



# Konfigurasi default untuk DAG
default_args = {
    'owner': 'dzikri',
    'start_date': datetime(2024, 4, 17),
    'retries': 1,
}

# Mendefinisikan DAG
dag = DAG(
    'eksplorasi_ingestion',
    default_args=default_args,
    description='Workflow untuk analisis data',
    schedule_interval='@daily',
    catchup=False
)

# Mendefinisikan operator-operatir di dalam DAG
extract_data_task = PythonOperator(
    task_id='extract_data',
    python_callable=download_dataset,
    dag=dag,
)

transform_data_task = PythonOperator(
    task_id='transform_data',
    python_callable=transform_data,
    provide_context=True,  # Untuk memberikan akses ke task instance (ti)
    dag=dag,
)

export_to_excel_task = PythonOperator(
    task_id='export_to_excel',
    python_callable=export_to_excel,
    provide_context=True,  # Untuk memberikan akses ke task instance (ti)
    dag=dag,
)

visualize_data_task = PythonOperator(
    task_id='visualize_data',
    python_callable=visualize_data,
    provide_context=True,  # Untuk memberikan akses ke task instance (ti)
    dag=dag,
)

# Mendefinisikan urutan task
extract_data_task >> transform_data_task >> export_to_excel_task >> visualize_data_task