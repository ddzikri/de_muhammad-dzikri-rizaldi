from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import requests
import json
import pandas as pd
import firebase_admin
from firebase_admin import credentials, initialize_app, storage

def extract_and_transform_data():
    url = 'https://fakestoreapi.com/products'
    response = requests.get(url)
    data = response.json()
    
    transformed_data = []
    for product in data:
        if float(product['price']) > 100: 
            transformed_data.append({
                'title': product['title'],
                'price': product['price'],
                'description': product['description'],
                'category': product['category']
            })
    
    return transformed_data

def save_data_to_csv():
    transformed_data = extract_and_transform_data()  
    df = pd.DataFrame(transformed_data)
    df.to_csv('transformed.csv', index=False)  

def load_data_to_firebase():
    cred = credentials.Certificate("/home/dzikri/airflow/serviceAccountKey.json")
    firebase_admin.initialize_app(cred, {"storageBucket": "data-engineering-in-the-cloud.appspot.com"})
    bucket = storage.bucket()

    df = pd.read_csv('transformed.csv')

    df.to_parquet('transformed.parquet', index=False)
 
    blob = bucket.blob("transformed.parquet")
    blob.upload_from_filename('transformed.parquet')

default_args = {
    'owner': 'dzikri',
    'depends_on_past': False,
    'start_date': datetime(2024, 4, 18),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1
}

with DAG('data_in_the_cloud', default_args=default_args, schedule_interval='@daily') as dag:
    extract_transform_task = PythonOperator(
        task_id='ekstrak_data',
        python_callable=extract_and_transform_data
    )

    save_data_task = PythonOperator(
        task_id='transform_data',
        python_callable=save_data_to_csv
    )

    load_data_task = PythonOperator(
        task_id='load_data',
        python_callable=load_data_to_firebase
    )
    
    extract_transform_task >> save_data_task >> load_data_task