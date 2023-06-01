from datetime import datetime, timedelta
from textwrap import dedent

import requests
from airflow import DAG

# Operators; we need this to operate!
from airflow.operators.bash import BashOperator
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import BranchPythonOperator
from airflow.operators.python_operator import PythonOperator
from airflow.utils.trigger_rule import TriggerRule

default_args = {
    'owner': 'owner-name',
    'depends_on_past': False,
    'email': ['your-email@g.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=15),
}

dag_args = dict(
    dag_id="call_trigger-test",
    default_args=default_args,
    description='test DAG python',
    schedule_interval=timedelta(minutes=50),
    start_date=datetime(2023, 6, 1),
    tags=['example-sj'],
)

def call_fast_api():
    import requests

    address_istio_gateway = 'http://34.68.103.239:80/'  # ingress gateway 주소
    result = requests.get(address_istio_gateway)
    print(result.text)

def call_torch_serving():
    import requests

    address_istio_gateway = 'http://34.68.103.239:80/predictions/densenet161'
    file_path = '../kitten.jpg'

    with open(file_path, 'rb') as f:
        response = requests.post(address_istio_gateway, data=f)

    print(response.content)

with DAG(**dag_args) as dag:
    start = BashOperator(
        task_id='start',
        bash_command='echo "start!"',
    )

    exec_trigger_1 = PythonOperator(
        task_id='complete_py',
        python_callable=call_fast_api,
        trigger_rule=TriggerRule.NONE_FAILED
    )

    exec_trigger_2 = PythonOperator(
        task_id='complete_py',
        python_callable=call_torch_serving,
        trigger_rule=TriggerRule.NONE_FAILED
    )

    complete = BashOperator(
        task_id='complete ',
        depends_on_past=False,
        bash_command='echo "complete~!"',
        trigger_rule=TriggerRule.NONE_FAILED
    )

    start >> exec_trigger_1 >> exec_trigger_2 >> complete



