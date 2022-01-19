import unittest
from datetime import datetime

from coin_data_manager.models.candle import Candle
from coin_data_manager.util import CandleUnit


class TestCandle(unittest.TestCase):
    def test_candle_equals(self):
        price = 10000.0
        acc_trade_volume = 1440
        acc_trade_price = price * acc_trade_volume

        market_a = "KRW-BTC"
        unit_a = CandleUnit.MIN_1
        candle_datetime_a = datetime(2021, 1, 10, 12, 30)

        market_b = "KRW-BTC"
        unit_b = CandleUnit.MIN_1
        candle_datetime_b = datetime(2021, 1, 10, 12, 30)

        market_c = "KRW-BTC"
        unit_c = CandleUnit.MIN_1
        candle_datetime_c = datetime(2021, 1, 10, 12, 29)

        candle_a = Candle(
            market=market_a,
            unit=unit_a,
            _datetime=candle_datetime_a,
            open_price=price,
            high_price=price,
            low_price=price,
            close_price=price,
            acc_trade_price=acc_trade_price,
            acc_trade_volume=acc_trade_volume,
        )
        candle_b = Candle(
            market=market_b,
            unit=unit_b,
            _datetime=candle_datetime_b,
            open_price=price,
            high_price=price,
            low_price=price,
            close_price=price,
            acc_trade_price=acc_trade_price,
            acc_trade_volume=acc_trade_volume,
        )
        candle_c = Candle(
            market=market_c,
            unit=unit_c,
            _datetime=candle_datetime_c,
            open_price=price,
            high_price=price,
            low_price=price,
            close_price=price,
            acc_trade_price=acc_trade_price,
            acc_trade_volume=acc_trade_volume,
        )

        self.assertTrue(candle_a == candle_b)
        self.assertFalse(candle_b == candle_c)
        self.assertFalse(candle_c == candle_a)

    def test_candle_sortable(self):
        price = 10000.0
        acc_trade_volume = 1440
        acc_trade_price = price * acc_trade_volume

        market_a = "KRW-BTC"
        unit_a = CandleUnit.MIN_1
        candle_datetime_a = datetime(2021, 1, 10, 12, 30)

        market_b = "KRW-BTC"
        unit_b = CandleUnit.MIN_1
        candle_datetime_b = datetime(2021, 1, 10, 12, 31)

        candle_a = Candle(
            market=market_a,
            unit=unit_a,
            _datetime=candle_datetime_a,
            open_price=price,
            high_price=price,
            low_price=price,
            close_price=price,
            acc_trade_price=acc_trade_price,
            acc_trade_volume=acc_trade_volume,
        )
        candle_b = Candle(
            market=market_b,
            unit=unit_b,
            _datetime=candle_datetime_b,
            open_price=price,
            high_price=price,
            low_price=price,
            close_price=price,
            acc_trade_price=acc_trade_price,
            acc_trade_volume=acc_trade_volume,
        )

        candles = [candle_b, candle_a]
        sorted_candles = sorted(candles)

        self.assertTrue(candle_a < candle_b)
        self.assertFalse(candle_b < candle_a)
        self.assertEqual([candle_a, candle_b], sorted_candles)


if __name__ == "__main__":
    unittest.main()
