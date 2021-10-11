# 설치 라이브러리
- pip install fastapi
- pip install uvicorn
- pip install hypercorn

# 실행 방법
- test.py 코드 입력
- uvicorn f_server:app --reload
- uvicorn test:app --reload 로 실행
<!-- - uvicorn test:app --reload --host=0.0.0.0 --port=8000 -->

# 호출
- http://127.0.0.1:8000/
