from datetime import datetime
from typing import Optional

from fastapi import FastAPI

from coin_data_manager.models.producer import ProducerData, Producer
from coin_data_manager.repositories.candle import CandleRepository
from coin_data_manager.repositories.producer import ProducerRepository
from coin_data_manager.repositories.repository import AlreadyExistError
from coin_data_manager.util import CandleUnit
from config.config import CONFIG

database_config = CONFIG["database_dev"]
app = FastAPI()


@app.get("/producer/")
def get_producers():
    """
    모든 producer 정보를 가져옵니다.
    :return:
    """
    producer_repository = ProducerRepository(**database_config)
    producers = producer_repository.get_all()

    return [producer.__dict__ for producer in producers]


@app.get("/candle")
def get_candle_date_counts(market: str, unit: str, from_datetime: Optional[str], to_datetime: Optional[str]):
    """
    :param market: 원하는 candle의 market code입니다. 예를 들어 한화 비트코인은 KRW-BTC 입니다.\n
    :param unit: 원하는 candle의 단위입니다. 분봉, 일봉, 주봉, 월봉이 있으며 월봉은 아래와 같이 여러 값들이 있습니다.\n

        - minutes/1, minutes/3, minutes/5, minutes/10, minutes/15, minutes/30, minutes/60, minutes/240
        - days
        - weeks
        - months
    :param from_datetime: candle이 시작하는 날짜입니다. 2021년 10월 19일 12시 30분은 다음과 같이 작성합니다. ex) 202110191230\n
    :param to_datetime: ex) 202110191230\n
    :return:
    """
    unit = CandleUnit(unit)
    from_datetime = datetime.strptime(from_datetime, "%Y%m%d%H%M")
    to_datetime = datetime.strptime(to_datetime, "%Y%m%d%H%M")

    candle_repository = CandleRepository(**database_config)
    candles = candle_repository.get_all(market,unit, from_datetime, to_datetime)

    return [candle.__dict__ for candle in candles]


@app.post("/producer/")
def create_producer(producer: ProducerData):
    """
    producer를 생성합니다.
    :param producer:
    :return:
    """
    producer_repository = ProducerRepository(**database_config)
    try:
        producer_repository.add(
            Producer(market=producer.market, unit=CandleUnit(producer.unit))
        )
    except AlreadyExistError:
        return "Already exist"


@app.delete("/producer/")
def delete_producer(producer: ProducerData):
    """
    producer를 제거합니다.
    :param producer:
    :return:
    """
    producer_repository = ProducerRepository(**database_config)
    producer_repository.delete(
        Producer(market=producer.market, unit=CandleUnit(producer.unit))
    )


@app.put("/producer/")
def update_producer(producer: ProducerData):
    """
    producer를 수정합니다.\n
    :param producer:
    :return:
    """
    producer_repository = ProducerRepository(**database_config)
    producer_repository.update(
        Producer(market=producer.market, unit=CandleUnit(producer.unit))
    )
