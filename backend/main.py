from typing import Optional
from fastapi import FastAPI

from coin_data_manager.repositories.producer import ProducerRepository
from config.config import CONFIG

database_config = CONFIG["database"]
producer_repository = ProducerRepository(**database_config)

app = FastAPI()


@app.get("/")
def read_root():
    producers = producer_repository.get_all()

    return [producer.__dict__ for producer in producers]


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
