from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import json
import requests
import logging

def insert_fruit_data_into_db(**kwargs):
    fruit_data = kwargs['ti'].xcom_pull(task_ids='get_fruit_data')
    hook = PostgresHook(
        postgres_conn_id='eksplorasi',
        username='airflow',
        password='airflow',
        host='localhost',
        port='5432',
        database='my_db'
    )
    conn = hook.get_conn()
    cur = conn.cursor()

    for fruit in fruit_data:
        cur.execute('''
            INSERT INTO fruits (name, calories, fat, sugar, carbohydrates, protein)
            VALUES (%s, %s, %s, %s, %s, %s);
        ''', (
            fruit['name'],
            fruit['nutritions']['calories'],
            fruit['nutritions']['fat'],
            fruit['nutritions']['sugar'],
            fruit['nutritions']['carbohydrates'],
            fruit['nutritions']['protein'],
        ))

    conn.commit()
    cur.close()

default_args = {
    'owner': 'dzikri',
    'start_date': datetime(2024, 4, 16),
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'eksplorasii_dag',
    default_args=default_args,
    schedule_interval=timedelta(days=1),
)

create_fruits_table = PostgresOperator(
    task_id='create_fruits_table',
    postgres_conn_id='eksplorasi_db',
    sql="""
        CREATE TABLE IF NOT EXISTS fruits (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50) NOT NULL,
            calories DECIMAL NOT NULL,
            fat DECIMAL NOT NULL,
            sugar DECIMAL NOT NULL,
            carbohydrates DECIMAL NOT NULL,
            protein DECIMAL NOT NULL
        );

        CREATE SEQUENCE IF NOT EXISTS fruits_id_seq
            START WITH 1
            INCREMENT BY 1
            NO MINVALUE
            NO MAXVALUE
            CACHE 1;
    """,
    dag=dag,
)

def get_api_data():
    try:
        response = requests.get("https://www.fruityvice.com/api/fruit/family/Rosaceae")
        response.raise_for_status()  
    except Exception as e:
        logging.error(f"Failed to fetch data from API: {e}")
        raise

get_fruit_data = PythonOperator(
    task_id='get_fruit_data',
    python_callable=get_api_data,
    dag=dag,
)

insert_fruit_data = PythonOperator(
    task_id='insert_fruit_data',
    python_callable=insert_fruit_data_into_db,
    provide_context=True,  
    dag=dag,
)

create_fruits_table >> get_fruit_data >> insert_fruit_data