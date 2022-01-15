from typing import Optional
from fastapi import FastAPI

from coin_data_manager.repositories.candle import CandleRepository
from coin_data_manager.repositories.producer import ProducerRepository
from config.config import CONFIG

database_config = CONFIG["database"]
producer_repository = ProducerRepository(**database_config)
candle_repository = CandleRepository(**database_config)
app = FastAPI()


@app.get("/")
def get_producers():
    producers = producer_repository.get_all()

    return [producer.__dict__ for producer in producers]


@app.get("/candle/date/{market}")
def get_candle_date_counts(market: str):
    candle_date_counts = candle_repository.get_date_count(market)

    return candle_date_counts


@app.post("/producer/{market}/{unit}/{minutes}")
def read_item(market: str, unit: str, minutes: Optional[int] = None):
    return market, unit, minutes
