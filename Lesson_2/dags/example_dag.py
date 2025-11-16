from datetime import datetime 
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator


def f():
    print("Это мой первый Python оператор!")


with DAG(dag_id='first_dag',
         start_date=datetime(2025, 11, 16),
         schedule_interval='@hourly',
         catchup=False) as dag:
    p_task = PythonOperator(task_id='py_1', python_callable=f)
    b_task = BashOperator(task_id='bf_1', bash_command='echo "Привет из консоли!"')

    # p_task >> b_task  # последовательный запуск тасков
    [p_task, b_task] 
