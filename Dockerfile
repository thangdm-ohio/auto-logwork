FROM python:3.11-alpine

WORKDIR /service

COPY requirements.txt /service/requirements.txt

RUN pip install -r requirements.txt

COPY .env.example /service/.env

COPY . /service/.

CMD sh runner.sh