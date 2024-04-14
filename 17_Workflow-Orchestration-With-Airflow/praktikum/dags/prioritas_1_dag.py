from datetime import datetime, timedelta
from airflow import DAG 
from airflow.operators.bash import BashOperator

default_args = {
    "owner": "dzikri",
    "retries": 5,
    "retry_delay": timedelta(minutes=2),
}

with DAG(
    dag_id="prioritas_1",
    default_args=default_args,
    description="prioritas_1",
    start_date=datetime(2024, 4, 12),
    schedule_interval='@daily',
) as dag:

    task1 = BashOperator(
        task_id="echo_hello_airflow",
        bash_command="echo hello airflow",
    )

    task2 = BashOperator(
        task_id="mkdir_our_work",
        bash_command="mkdir -p /opt/airflow/dags/our_works",  
    )

    task3 = BashOperator(
        task_id="mkdir_about_us",
        bash_command="mkdir -p /opt/airflow/dags/about_us",  
    )

    task4 = BashOperator(
        task_id="touch_our_works",
        bash_command="touch /opt/airflow/dags/our_works/works.txt",  # Ubah path sesuai direktori DAG
        trigger_rule="all_success",
    )

    task5 = BashOperator(
        task_id="touch_about_us",
        bash_command="touch /opt/airflow/dags/about_us/about.txt",  # Ubah path sesuai direktori DAG
        trigger_rule="all_success",
    )

    task6 = BashOperator(
        task_id="echo_done",
        bash_command="echo done!",
    )

    task1 >> [task2, task3]  

    task2 >> task4 

    task3 >> task5 

    [task4, task5] >> task6