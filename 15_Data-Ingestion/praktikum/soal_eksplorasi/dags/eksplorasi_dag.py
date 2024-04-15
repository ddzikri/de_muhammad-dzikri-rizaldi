from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import requests
import pandas as pd

def extract_book_data():
    url = 'https://gist.githubusercontent.com/nadirbslmh/8922f71875948802321ef479a017f4c0/raw/1fbbc4b3d55f8ae717eb197d9aaf530ed1bc7ed2/sample.json'
    
    try:
        response = requests.get(url)
        response.raise_for_status()  
        data = response.json()
        
        if data.get('status') and isinstance(data.get('data'), list):
            relevant_books = []
            for book in data['data']:
                relevant_books.append({
                    'judul': book['title'],
                    'pengarang': book['author'],
                    'tahun_terbit': book['year'],
                    'genre': book['genre']
                })
            return relevant_books
        else:
            print("Data buku tidak ditemukan atau format respons tidak valid.")
            return []
    
    except requests.exceptions.RequestException as e:
        print(f"Error saat melakukan permintaan API: {e}")
        return []

    
default_args = {
    'owner': 'dzikri',
    'depends_on_past': False,
    'start_date': datetime(2024, 4, 14), 
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'eksplorasi_data_ingestion',
    default_args=default_args,
    description='DAG to extract data buku from an API',
    schedule_interval='0 9 * * 1',  
    catchup=False
)

def extract_and_process(**kwargs):
    relevant_books = extract_book_data()
    
    # Konversi relevant_books ke DataFrame pandas
    df = pd.DataFrame(relevant_books, columns=['judul', 'pengarang', 'tahun_terbit', 'genre'])
    
    # Cetak sebagian data ke log Airflow
    if not df.empty:
        print("Extracted books (head):")
        print(df.head())
        print("Extracted books (tail):")
        print(df.tail())
    else:
        print("Tidak ada data buku yang diekstrak atau format respons tidak valid.")

extract_task = PythonOperator(
    task_id='extract_task',
    python_callable=extract_and_process,
    dag=dag
)
