import os
import time
from datetime import datetime

from coin_data_manager.api.api_caller import UpbitApiCaller
from coin_data_manager.repositories.candle import CandleRepository, AlreadyExistError
from coin_data_manager.util import CandleUnit, TooManyRequestsError
from config.config import CONFIG

if __name__ == "__main__":
    market = os.environ["MARKET"]
    print("market", market)

    database_config = CONFIG["database"]

    database = database_config["database"]
    host = database_config["host"]
    port = database_config["port"]
    user = database_config["user"]
    password = database_config["password"]

    candle_repository = CandleRepository(database, host, port, user, password)
    api_caller = UpbitApiCaller()
    start_datetime = datetime.utcnow()
    while True:
        try:
            candles = api_caller.get_candles(
                market,
                1,
                CandleUnit.MIN_1,
                to=datetime.utcnow().strftime("%Y-%m-%d %H:%M:00"),
            )

            candle = candles[0]
            print(candle)

            try:
                candle_repository.add(candle)
            except AlreadyExistError as e:
                print("Already")

            time.sleep(50)
        except TooManyRequestsError as e:
            print(e)
            time.sleep(1)

