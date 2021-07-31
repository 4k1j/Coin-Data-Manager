# Dockerfile for test

FROM python:3.9-slim-buster


COPY . .

RUN pip3 install --upgrade pip

RUN pip3 install -r requirements.txt

RUN python3 coin/setup.py develop


CMD ["python3", "tests/api/TestUpbitQuotationApiCaller.py"]