FROM python:3.9-slim

RUN mkdir /app

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

CMD FLASK_APP=app.py flask run