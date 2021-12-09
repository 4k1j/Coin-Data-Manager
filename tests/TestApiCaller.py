import unittest

from coin_data_manager.api.api_caller import UpbitApiCaller, SimpleApiCaller
from coin_data_manager.util import CandleUnit


class TestApiCaller(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.api_caller = SimpleApiCaller()

    def test_get_candles(self):
        market = "KRW-BTC"
        count = 10
        unit = CandleUnit.MIN_1
        candles = self.api_caller.get_candles(market, count, unit)

        self.assertEqual(count, len(candles))

        for candle in candles:
            self.assertEqual(unit, candle.unit)

    def test_get_ticker(self):
        pass


class TestUpbitApiCaller(TestApiCaller):
    @classmethod
    def setUpClass(cls) -> None:
        cls.api_caller = UpbitApiCaller()


if __name__ == "__main__":
    unittest.main()
