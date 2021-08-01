import unittest

from coin.api.UpbitQuotationApiCaller import UpbitQuotationApiCaller
from coin.candle.Candle import Candle
from coin.candle.upbit.UpbitDayCandle import UpbitDayCandle
from coin.candle.upbit.UpbitMinuteCandle import UpbitMinuteCandle
from coin.candle.upbit.UpbitMonthCandle import UpbitMonthCandle
from coin.candle.upbit.UpbitWeekCandle import UpbitWeekCandle
from coin.tick.Tick import Tick
from coin.tick.Ticker import Ticker


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

    def test_get_ticks(self):
        ticks = self.api_caller.get_ticks("KRW-BTC", 10)
        tick = ticks[0]

        self.assertTrue(len(ticks) == 10)
        self.assertTrue(isinstance(tick, Tick))

        for _, value in tick.__dict__.items():
            self.assertTrue(value is not None)

    def test_get_tickers(self):
        markets = ["KRW-BTC", "BTC-ETH"]
        tickers = self.api_caller.get_tickers(markets)

        self.assertTrue(len(tickers) == len(markets))

        krw_btc_ticker = tickers[0]
        btc_eth_ticker = tickers[1]

        self.assertTrue(isinstance(krw_btc_ticker, Ticker))
        self.assertTrue(isinstance(btc_eth_ticker, Ticker))

        for _, value in krw_btc_ticker.__dict__.items():
            self.assertTrue(value is not None)

        for _, value in btc_eth_ticker.__dict__.items():
            self.assertTrue(value is not None)


if __name__ == "__main__":
    unittest.main()
