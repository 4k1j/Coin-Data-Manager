from fastapi.testclient import TestClient
import unittest

from coin_data_manager.models.producer import Producer
from coin_data_manager.repositories.producer import ProducerRepository
from coin_data_manager.util import CandleUnit
from config.config import CONFIG
from main import app


class TestProducer(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.client = TestClient(app)
        database_config = CONFIG["database_dev"]
        cls.producer_repository = ProducerRepository(**database_config)

    def test_add_producer(self):
        test_producer = Producer(
            "KRW-DOGE", CandleUnit.MIN_10
        )

        producer_info = {
            "market": test_producer.market,
            "unit": test_producer.unit.value
        }

        self.client.post(
            "/producer/",
            json=producer_info
        )

        producer = self.producer_repository.get(
            test_producer
        )

        self.assertEqual(test_producer, producer)

    @classmethod
    def tearDownClass(cls) -> None:
        database_config = CONFIG["database_dev"]
        producer_repository = ProducerRepository(**database_config)

        test_producers = [
            Producer(
                "KRW-DOGE", CandleUnit.MIN_10
            )
        ]

        for test_producer in test_producers:
            producer_repository.delete(test_producer)
