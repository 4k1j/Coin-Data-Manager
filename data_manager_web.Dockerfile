FROM python:3.8-slim-buster


RUN apt-get update
RUN mkdir ./coin-data-manager

COPY . ./coin-data-manager

WORKDIR coin-data-manager
COPY web .

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]