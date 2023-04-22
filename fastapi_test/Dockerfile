FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY ./server.py /app

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "30000"]