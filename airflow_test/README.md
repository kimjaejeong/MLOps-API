- dag파일
  - call_trigger_dag.py
    - api call 하기 위한 스케줄러
  - run_jar_dag.py
    - jar 파일 실행을 위한 스케줄러
- 참고자료
  - https://github.com/lsjsj92/airflow_tutorial 
  - https://passwd.tistory.com/m/entry/Apache-Airflow-%EC%84%A4%EC%B9%98

- 스케줄 관련 .py를 ~/airflow/dags 하위에 넣고 airflow webserver로 재실행


- 스케줄 시나리오
  - 외부 url call
  - 내부 jar 파일 실행