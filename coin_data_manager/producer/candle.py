from datetime import datetime
from kafka import KafkaProducer
from json import dumps
import time

from coin_data_manager.models.producer import Producer
from coin_data_manager.api.api_caller import UpbitApiCaller
from coin_data_manager.repositories.producer import ProducerRepository
from coin_data_manager.util import TooManyRequestsError, CandleUnit


class CandleProducer:
    def __init__(self, market: str, unit: CandleUnit, broker_host: str, database_config: dict, env="dev"):
        self.market = market
        self.unit = unit
        self.topic = f"coin-bot.coin-data-manager.{env}.{market}"
        self.model = Producer(market, unit)
        self.producer = KafkaProducer(
            acks=0,
            compression_type="gzip",
            bootstrap_servers=[f"{broker_host}:9092"],
            value_serializer=lambda x: dumps(x).encode("utf-8"),
        )

        self.producer_repository = ProducerRepository(**database_config)

        self.api_caller = UpbitApiCaller()

    def produce(self):

        count = 0
        while True:
            try:
                candles = self.api_caller.get_candles(
                    f"{self.market}",
                    1,
                    self.unit,
                    to=datetime.utcnow().strftime("%Y-%m-%d %H:%M:00"),
                )

                candle = candles[0]
                print(candle.__dict__)
                response = self.producer.send(self.topic, value=candle.__dict__)
                print("response : ", response.get(3))
                self.producer.flush()

                time.sleep(50)
                count += 1
            except TooManyRequestsError as e:
                print(e)
                time.sleep(1)

            if count > 10:
                self.model.heartbeat = datetime.utcnow()
                self.producer_repository.update(self.model)
