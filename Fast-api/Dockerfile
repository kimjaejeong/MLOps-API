FROM python:3.7
EXPOSE 80
COPY ./app /app
# COPY .env .env
COPY requirements.txt /app/requirements.txt

WORKDIR /app
RUN python3 -m pip install --no-cache-dir --upgrade \
        setuptools \
        wheel \
        && \
    python3 -m pip install --trusted-host pypi.python.org -r requirements.txt

CMD ["uvicorn", "04_server:app", "--host", "0.0.0.0", "--port", "80"]