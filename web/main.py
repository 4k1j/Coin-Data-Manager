from fastapi import FastAPI

from coin_data_manager.models.producer import ProducerData, Producer
from coin_data_manager.repositories.candle import CandleRepository
from coin_data_manager.repositories.producer import ProducerRepository
from coin_data_manager.repositories.repository import AlreadyExistError
from coin_data_manager.util import CandleUnit
from config.config import CONFIG

database_config = CONFIG["database_dev"]
app = FastAPI()


@app.get("/")
def get_producers():
    producer_repository = ProducerRepository(**database_config)
    producers = producer_repository.get_all()

    return [producer.__dict__ for producer in producers]


@app.get("/candle/date/{market}")
def get_candle_date_counts(market: str):
    candle_repository = CandleRepository(**database_config)
    candle_date_counts = candle_repository.get_date_count(market)

    return candle_date_counts


@app.post("/producer/")
def create_producer(producer: ProducerData):
    producer_repository = ProducerRepository(**database_config)
    try:
        producer_repository.add(
            Producer(market=producer.market, unit=CandleUnit(producer.unit))
        )
    except AlreadyExistError:
        return "Already exist"


@app.delete("/producer/")
def delete_producer(producer: ProducerData):
    producer_repository = ProducerRepository(**database_config)
    producer_repository.delete(
        Producer(market=producer.market, unit=CandleUnit(producer.unit))
    )


@app.put("/producer/")
def update_producer(producer: ProducerData):
    producer_repository = ProducerRepository(**database_config)
    producer_repository.update(
        Producer(market=producer.market, unit=CandleUnit(producer.unit))
    )
