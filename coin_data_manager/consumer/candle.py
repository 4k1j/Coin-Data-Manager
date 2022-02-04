import json

from kafka import KafkaConsumer
from json import loads  # topic, broker list

from coin_data_manager.models.candle import Candle
from coin_data_manager.repositories.candle import CandleRepository
from coin_data_manager.repositories.repository import AlreadyExistError
from coin_data_manager.util import CandleUnit


class CandleConsumer:
    def __init__(self, market: str,
                 unit: CandleUnit,
                 broker_host: str,
                 database_config: dict,
                 env="dev", ):
        self.market = market
        self.unit = unit
        self.env = env
        self.topic = f"coin-bot.coin-data-manager.{env}.{market}"
        self.consumer = KafkaConsumer(
            self.topic,
            bootstrap_servers=[f"{broker_host}:9092"],
            auto_offset_reset="earliest",  # latest, earliest
            # enable_auto_commit=True,
            # group_id="my-group",
            value_deserializer=lambda x: loads(x.decode("utf-8")),
            # consumer_timeout_ms=1000,
        )
        self.candle_repository = CandleRepository(**database_config)

    def consume(self):
        for message in self.consumer:
            print(f"Offset : {message.offset}")

            value = message.value
            if type(value) == str:
                value = json.load(message.value)

            candle = Candle(
                market=value["market"],
                unit=value["unit"],
                _datetime=value["datetime"],
                open_price=value["open_price"],
                high_price=value["high_price"],
                low_price=value["low_price"],
                close_price=value["close_price"],
                acc_trade_price=value["acc_trade_price"],
                acc_trade_volume=value["acc_trade_volume"],
            )

            print(candle)
            try:
                self.candle_repository.add(candle)
            except AlreadyExistError:
                print(f"Already candle : {candle}")


