from datetime import datetime, timedelta
from textwrap import dedent

from airflow import DAG

# Operators; we need this to operate!
from airflow.operators.bash import BashOperator
# from airflow.operators.dummy import DummyOperator
from airflow.operators.python import BranchPythonOperator, PythonOperator
# from airflow.operators.python_operator import PythonOperator
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
    dag_id="jar-test",
    default_args=default_args,
    description='test DAG java',
    schedule_interval=timedelta(minutes=50),
    start_date=datetime(2023, 5, 25),
    tags=['example-sj'],
)

# .sh을 통해 .jar 파일 배치 실행으로 수정
with DAG(**dag_args) as dag:
    start = BashOperator(
        task_id='start',
        bash_command='echo "start!"',
    )

    # msg = PythonOperator(
    #     task_id='call_url',
    #     python_callable=call_url,
    #     trigger_rule=TriggerRule.NONE_FAILED
    # )

    # public cloud 배치1
    exec_jar1 = BashOperator(
        task_id='api_jar_test1',
        bash_command='java -jar ../api-0.0.1-SNAPSHOT.jar'
    )

    # public cloud 배치2
    exec_jar2 = BashOperator(
        task_id='api_jar_test2',
        bash_command='java -jar ../api-0.0.1-SNAPSHOT.jar'
    )

    # public cloud 배치3
    exec_jar3 = BashOperator(
        task_id='api_jar_test3',
        bash_command='java -jar ../api-0.0.1-SNAPSHOT.jar'
    )

    complete = BashOperator(
        task_id='complete_bash',
        depends_on_past=False,
        bash_command='echo "complete~!"',
        trigger_rule=TriggerRule.NONE_FAILED
    )

    start >> exec_jar1 >> exec_jar2 >> exec_jar3 >> complete