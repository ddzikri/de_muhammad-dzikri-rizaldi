from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from random import sample
from collections import Counter

default_args = {
    'owner': 'dzikri',
    'depends_on_past': False,
    'start_date': datetime(2024, 4, 12),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'prioritas_1_no_2', default_args=default_args, schedule_interval=timedelta(1))

def generate_random_numbers():
    numbers = sample(range(1, 51), 25)
    return numbers

def calculate_sum(ti):
    numbers = ti.xcom_pull(task_ids='generate_random_numbers', key='return_value')
    total = sum(numbers)
    ti.xcom_push(key='sum_of_numbers', value=total)

def check_even_sum(ti):
    total = ti.xcom_pull(task_ids='calculate_sum', key='sum_of_numbers')
    if total % 2 == 0:
        result = 'Even Sum'
    else:
        result = 'Odd Sum'
    print(result)

t1 = PythonOperator(
    task_id='generate_random_numbers',
    python_callable=generate_random_numbers,
    dag=dag)

t2 = PythonOperator(
    task_id='calculate_sum',
    python_callable=calculate_sum,
    provide_context=True,
    dag=dag)

t3 = PythonOperator(
    task_id='check_even_sum',
    python_callable=check_even_sum,
    dag=dag)

t1 >> t2 >> t3
