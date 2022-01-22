import unittest
from datetime import datetime

from coin_data_manager.models.candle import Candle
from coin_data_manager.repositories.candle import CandleRepository
from coin_data_manager.repositories.repository import NotFoundError
from coin_data_manager.util import CandleUnit
from config.config import CONFIG


class TestRepository(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        database_config = CONFIG["database"]
        candle_repository = CandleRepository(**database_config)

        test_candles = [
            Candle(
                market="KRW-BTC",
                unit=CandleUnit.MIN_1,
                _datetime=datetime(1996, 3, 2, 12, 30),
                open_price=10000.9,
                high_price=10001.1,
                low_price=9000.2,
                close_price=10030.2,
                acc_trade_price=215123152.2,
                acc_trade_volume=125125,
            ),
            Candle(
                market="KRW-BTC",
                unit=CandleUnit.MIN_1,
                _datetime=datetime(1996, 3, 3, 12, 30),
                open_price=10000.9,
                high_price=10001.1,
                low_price=9000.2,
                close_price=10030.2,
                acc_trade_price=215123152.2,
                acc_trade_volume=125125,
            ),
        ]

        for test_candle in test_candles:
            candle_repository.add(test_candle)

        cls.candle_repository = candle_repository

    def test_get_candle(self):
        target_candle = Candle(
            market="KRW-BTC",
            unit=CandleUnit.MIN_1,
            _datetime=datetime(1996, 3, 2, 12, 30),
            open_price=10000.9,
            high_price=10001.1,
            low_price=9000.2,
            close_price=10030.2,
            acc_trade_price=215123152.2,
            acc_trade_volume=125125,
        )

        candle = self.candle_repository.get(target_candle)

        self.assertEqual(target_candle, candle)
        self.assertEqual(target_candle.open_price, candle.open_price)
        self.assertEqual(target_candle.high_price, candle.high_price)
        self.assertEqual(target_candle.low_price, candle.low_price)
        self.assertEqual(target_candle.close_price, candle.close_price)
        self.assertEqual(target_candle.acc_trade_price, candle.acc_trade_price)
        self.assertEqual(target_candle.acc_trade_volume, candle.acc_trade_volume)

    def test_delete_candle(self):
        target_candle = Candle(
            market="KRW-BTC",
            unit=CandleUnit.MIN_1,
            _datetime=datetime(1996, 3, 3, 12, 30),
            open_price=10000.9,
            high_price=10001.1,
            low_price=9000.2,
            close_price=10030.2,
            acc_trade_price=215123152.2,
            acc_trade_volume=125125,
        )

        candle = self.candle_repository.get(target_candle)
        self.assertEqual(target_candle, candle)

        self.candle_repository.delete(target_candle)

        self.assertRaises(NotFoundError, self.candle_repository.get, candle)

    def test_add_candle(self):
        test_candle = Candle(
            market="KRW-BTC",
            unit=CandleUnit.MIN_1,
            _datetime=datetime(1996, 3, 4, 12, 30),
            open_price=10000.9,
            high_price=10001.1,
            low_price=9000.2,
            close_price=10030.2,
            acc_trade_price=215123152.2,
            acc_trade_volume=125125,
        )

        self.candle_repository.add(test_candle)

        candle = self.candle_repository.get(test_candle)

        self.assertEqual(test_candle, candle)

    @classmethod
    def tearDownClass(cls) -> None:
        database_config = CONFIG["database"]
        cls.candle_repository = CandleRepository(**database_config)

        candle_repository = CandleRepository(**database_config)

        test_candles = [
            Candle(
                market="KRW-BTC",
                unit=CandleUnit.MIN_1,
                _datetime=datetime(1996, 3, 2, 12, 30),
                open_price=10000.9,
                high_price=10001.1,
                low_price=9000.2,
                close_price=10030.2,
                acc_trade_price=215123152.2,
                acc_trade_volume=125125,
            ),
            Candle(
                market="KRW-BTC",
                unit=CandleUnit.MIN_1,
                _datetime=datetime(1996, 3, 3, 12, 30),
                open_price=10000.9,
                high_price=10001.1,
                low_price=9000.2,
                close_price=10030.2,
                acc_trade_price=215123152.2,
                acc_trade_volume=125125,
            ),
            Candle(
                market="KRW-BTC",
                unit=CandleUnit.MIN_1,
                _datetime=datetime(1996, 3, 4, 12, 30),
                open_price=10000.9,
                high_price=10001.1,
                low_price=9000.2,
                close_price=10030.2,
                acc_trade_price=215123152.2,
                acc_trade_volume=125125,
            )
        ]

        for test_candle in test_candles:
            candle_repository.delete(test_candle)

        cls.candle_repository = candle_repository
