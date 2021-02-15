# FROM python:3.7
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
# WORKDIR /usr/src/api
WORKDIR /app/

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

ENV PYTHONPATH=/app/

COPY ./app /app/app
COPY ./alembic /app/alembic
COPY ./alembic.ini /app/alembic.ini

WORKDIR /app/app/

CMD alembic -c /app/alembic.ini upgrade head && uvicorn app.main:app --host 0.0.0.0 --port 8080 --reload