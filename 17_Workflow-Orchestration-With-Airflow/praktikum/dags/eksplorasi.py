from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import json
import requests
import logging

# Define the function to insert fruit data into the database
def insert_fruit_data_into_db(**kwargs):
    fruit_data = kwargs['ti'].xcom_pull(task_ids='get_fruit_data')
    hook = PostgresHook(postgres_conn_id='eksplorasi_postgres')
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

# Set default arguments for the DAG
default_args = {
    'owner': 'dzikri',
    'start_date': datetime(2024, 4, 12),  # Perbaikan tanggal start_date
    'retry_delay': timedelta(minutes=5),
}

# Create the DAG
dag = DAG(
    'eksplorasii_dag',
    default_args=default_args,
    schedule_interval=timedelta(days=1),
)

# Task 1: Create the fruits table
create_fruits_table = PostgresOperator(
    task_id='create_fruits_table',
    postgres_conn_id='eksplorasi',
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

        -- Perbaikan: Menambahkan sequence fruits_id_seq
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
        response.raise_for_status()  # Angkat eksepsi jika respons tidak sukses (status code >= 400)
        return response.json()
    except Exception as e:
        logging.error(f"Failed to fetch data from API: {e}")
        raise

# Task 2: Get data from API
get_fruit_data = PythonOperator(
    task_id='get_fruit_data',
    python_callable=get_api_data,
    dag=dag,
)

# Task 3: Insert fruit data into the fruits table
insert_fruit_data = PythonOperator(
    task_id='insert_fruit_data',
    python_callable=insert_fruit_data_into_db,
    provide_context=True,  # Memberikan konteks untuk mengakses XCom
    dag=dag,
)

# Set task dependencies
create_fruits_table >> get_fruit_data >> insert_fruit_data