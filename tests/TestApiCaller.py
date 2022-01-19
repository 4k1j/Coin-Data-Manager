import unittest
from datetime import datetime, timedelta

from coin_data_manager.api.api_caller import UpbitApiCaller
from coin_data_manager.util import CandleUnit


class TestApiCaller(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.api_caller = UpbitApiCaller()

    def test_get_specific_candle(self):
        target_datetime = datetime(2021, 8, 10, 18, 36)
        market = "KRW-BTC"
        count = 1
        unit = CandleUnit.MIN_1

        candles = self.api_caller.get_candles(
            market=market,
            count=count,
            unit=unit,
            to=target_datetime + timedelta(minutes=1)
        )

        self.assertEqual(count, len(candles))

        candle = candles[0]

        self.assertEqual(target_datetime, candle.datetime)
        self.assertEqual(market, candle.market)
        self.assertEqual(unit, candle.unit)


if __name__ == "__main__":
    unittest.main()
