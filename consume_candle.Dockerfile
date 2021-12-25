# extract_upbit_candles.Dockerfile for test

FROM python:3.8-slim-buster


RUN apt-get update
RUN mkdir ./coin-data-manager

COPY . ./coin-data-manager


WORKDIR coin-data-manager
COPY ./scripts .


RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt


CMD ["python3", "consume_candle.py"]