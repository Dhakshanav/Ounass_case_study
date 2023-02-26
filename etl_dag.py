from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime,timedelta
import os

dag = DAG(dag_id="etl_pipeline",schedule_interval=timedelta(days=1), start_date=datetime(2023, 2, 25),catchup=False,  tags=["running ETL pipeline"])

run_script = PythonOperator(task_id = 'etl_pipeline', python_callable=lambda: os.system('python3 ~/airflow/dags/etl/load.py'),dag=dag)
