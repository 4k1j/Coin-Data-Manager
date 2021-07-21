import time
from datetime import datetime

import pandas as pd

from main.api.UpbitQuotationApiCaller import UpbitQuotationApiCaller


def test_get_min_candles():
    api_caller = UpbitQuotationApiCaller()

    to = str(datetime.utcnow())[:19]

    while True:
        candles = api_caller.get_candle("KRW-BTC", count=200, to=to)
        if len(candles) < 1:
            break

        pd.json_normalize(candles).to_csv("../../data/KRW-BTC.csv", mode="a", header=False, index=False)

        to = candles[-1]["candle_date_time_utc"].replace("T", " ")
        time.sleep(0.11)


def test_get_ticker():
    api_caller = UpbitQuotationApiCaller()

    print(api_caller.get_ticker("KRW-BTC"))

test_get_ticker()