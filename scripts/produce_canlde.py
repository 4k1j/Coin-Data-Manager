from datetime import datetime
import os
from kafka import KafkaProducer
from json import dumps
import time

from coin_data_manager.api.api_caller import UpbitApiCaller
from coin_data_manager.util import CandleUnit, TooManyRequestsError
from config.config import CONFIG

if __name__ == '__main__':
    market = os.environ["MARKET"]
    env = os.environ["ENV"]
    kafka_config = CONFIG["kafka"]
    topic = f"coin-bot.coin-data-manager.{env}.{market}"
    print(f"Producer init : {topic}")

    producer = KafkaProducer(
        acks=0,
        compression_type="gzip",
        bootstrap_servers=[f"{kafka_config['broker']['host']}:9092"],
        value_serializer=lambda x: dumps(x).encode("utf-8"),
    )

    api_caller = UpbitApiCaller()
    start_datetime = datetime.utcnow()
    while True:
        try:
            candles = api_caller.get_candles(
                f"{market}",
                1,
                CandleUnit.MIN_1,
                to=datetime.utcnow().strftime("%Y-%m-%d %H:%M:00"),
            )

            candle = candles[0]
            print(candle.__dict__)
            producer.send(topic, value=candle.__dict__)
            producer.flush()

            time.sleep(40)
        except TooManyRequestsError as e:
            print(e)
            time.sleep(1)


