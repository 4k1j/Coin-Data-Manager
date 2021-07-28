import unittest

from main.api.UpbitQuotationApiCaller import UpbitQuotationApiCaller
from main.candle.Candle import Candle
from main.candle.upbit.UpbitDayCandle import UpbitDayCandle
from main.candle.upbit.UpbitMinuteCandle import UpbitMinuteCandle
from main.candle.upbit.UpbitMonthCandle import UpbitMonthCandle
from main.candle.upbit.UpbitWeekCandle import UpbitWeekCandle


class TestUpbitQuotationApiCaller(unittest.TestCase):
    def setUp(self):
        self.api_caller = UpbitQuotationApiCaller()

    def test_get_minutes_candle(self):
        candles = self.api_caller.get_candles("KRW-BTC", 1, "minutes/1")
        candle = candles[0]

        self.assertTrue(isinstance(candle, Candle))
        self.assertTrue(isinstance(candle, UpbitMinuteCandle))

        for _, value in candle.__dict__.items():
            self.assertTrue(value is not None)

    def test_get_days_candle(self):
        candles = self.api_caller.get_candles("KRW-BTC", 1, unit="days")
        candle = candles[0]

        self.assertTrue(isinstance(candle, Candle))
        self.assertTrue(isinstance(candle, UpbitDayCandle))

        for _, value in candle.__dict__.items():
            self.assertTrue(value is not None)

    def test_get_weeks_candle(self):
        candles = self.api_caller.get_candles("KRW-BTC", 1, unit="weeks")
        candle = candles[0]

        self.assertTrue(isinstance(candle, Candle))
        self.assertTrue(isinstance(candle, UpbitWeekCandle))

        for _, value in candle.__dict__.items():
            self.assertTrue(value is not None)

    def test_get_months_candle(self):
        candles = self.api_caller.get_candles("KRW-BTC", 1, unit="months")
        candle = candles[0]

        self.assertTrue(isinstance(candle, Candle))
        self.assertTrue(isinstance(candle, UpbitMonthCandle))

        for _, value in candle.__dict__.items():
            self.assertTrue(value is not None)


if __name__ == "__main__":
    unittest.main()
