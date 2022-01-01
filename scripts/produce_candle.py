import os

from coin_data_manager.producer.candle import CandleProducer
from coin_data_manager.util import CandleUnit
from config.config import CONFIG

if __name__ == '__main__':
    market = os.environ["MARKET"]
    env = os.environ["ENV"]
    kafka_config = CONFIG["kafka"]
    database_config = CONFIG["database"]
    topic = f"coin-bot.coin-data-manager.{env}.{market}"
    candle_producer = CandleProducer(market, CandleUnit.MIN_1, kafka_config['broker']['host'], database_config, env)
    candle_producer.produce()
