import unittest
from datetime import datetime, timedelta

from coin_data_manager.models.candle import Candle
from coin_data_manager.models.producer import Producer
from coin_data_manager.repositories.candle import CandleRepository
from coin_data_manager.repositories.producer import ProducerRepository
from coin_data_manager.repositories.repository import NotFoundError, AlreadyExistError
from coin_data_manager.util import CandleUnit
from config.config import CONFIG


class TestCandleRepository(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        database_config = CONFIG["database_dev"]
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

        sequential_candles = [
            Candle(
                market="KRW-BTC",
                unit=CandleUnit.MIN_10,
                _datetime=datetime(1996, 3, 4, 12, 30) + timedelta(minutes=i),
                open_price=1000 + i,
                high_price=1000 + i,
                low_price=1000 + i,
                close_price=1000 + i,
                acc_trade_price=1000 + i,
                acc_trade_volume=1000 + i,
            )
            for i in range(10)
        ]

        test_candles.extend(sequential_candles)
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

    def test_get_candles(self):
        market = "KRW-BTC"
        unit = CandleUnit.MIN_10
        from_datetime = datetime(1996, 3, 4, 12, 30)
        to_datetime = datetime(1996, 3, 4, 12, 39)

        candles = self.candle_repository.get_all(market, unit, from_datetime, to_datetime)

        self.assertEqual(10, len(candles))

        expect_candle = Candle(
            market=market,
            unit=unit,
            _datetime=from_datetime,
            open_price=1000.0,
            high_price=1000.0,
            low_price=1000.0,
            close_price=1000.0,
            acc_trade_price=1000.0,
            acc_trade_volume=1000.0,
        )

        test_count = 0
        candles.sort()
        for candle in candles:
            print(candle)
            self.assertEqual(expect_candle, candle)
            expect_candle.datetime += timedelta(minutes=1)

            self.assertEqual(expect_candle.open_price + test_count, candle.open_price)
            self.assertEqual(expect_candle.close_price + test_count, candle.close_price)
            self.assertEqual(expect_candle.low_price + test_count, candle.low_price)
            self.assertEqual(expect_candle.high_price + test_count, candle.high_price)
            self.assertEqual(
                expect_candle.acc_trade_price + test_count, candle.acc_trade_price
            )
            self.assertEqual(
                expect_candle.acc_trade_volume + test_count, candle.acc_trade_volume
            )

            test_count += 1

    @classmethod
    def tearDownClass(cls) -> None:
        database_config = CONFIG["database_dev"]
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
            ),
        ]

        sequential_candles = [
            Candle(
                market="KRW-BTC",
                unit=CandleUnit.MIN_10,
                _datetime=datetime(1996, 3, 4, 12, 30) + timedelta(minutes=i),
                open_price=1000 + i,
                high_price=1000 + i,
                low_price=1000 + i,
                close_price=1000 + i,
                acc_trade_price=1000 + i,
                acc_trade_volume=1000 + i,
            )
            for i in range(10)
        ]

        test_candles.extend(sequential_candles)

        for test_candle in test_candles:
            candle_repository.delete(test_candle)


class TestProducerRepository(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        database_config = CONFIG["database_dev"]
        producer_repository = ProducerRepository(**database_config)

        test_producers = [
            Producer("KRW-BTC", CandleUnit.MIN_1),
            Producer("KRW-ETH", CandleUnit.MIN_10),
        ]

        for test_producer in test_producers:
            producer_repository.add(test_producer)

        cls.producer_repository = producer_repository

    def test_get_producer(self):
        target_producer = Producer("KRW-BTC", CandleUnit.MIN_1)

        producer = self.producer_repository.get(target_producer)

        self.assertEqual(target_producer, producer)

    def test_add_producer(self):
        test_producer = Producer("KRW-DOGE", CandleUnit.MIN_1)

        self.producer_repository.add(test_producer)

        producer = self.producer_repository.get(test_producer)

        self.assertEqual(test_producer, producer)

        self.assertRaises(
            AlreadyExistError, self.producer_repository.add, test_producer
        )

    def test_delete_producer(self):
        target_producer = Producer("KRW-ETH", CandleUnit.MIN_10)

        self.producer_repository.delete(target_producer)

        self.assertRaises(NotFoundError, self.producer_repository.get, target_producer)

    def test_update_producer(self):
        target_producer = Producer("KRW-BTC", CandleUnit.MIN_1)
        order = "SLEEP 10"

        producer = self.producer_repository.get(target_producer)

        self.assertEqual(None, producer.order)

        target_producer.order = order

        self.producer_repository.update(target_producer)
        producer = self.producer_repository.get(target_producer)

        self.assertEqual(target_producer, producer)
        self.assertEqual(target_producer.order, producer.order)

    @classmethod
    def tearDownClass(cls) -> None:
        database_config = CONFIG["database_dev"]
        producer_repository = ProducerRepository(**database_config)

        test_producers = [
            Producer("KRW-BTC", CandleUnit.MIN_1),
            Producer("KRW-ETH", CandleUnit.MIN_10),
            Producer("KRW-DOGE", CandleUnit.MIN_1),
        ]

        for test_producer in test_producers:
            producer_repository.delete(test_producer)


if __name__ == "__main__":
    unittest.main()
