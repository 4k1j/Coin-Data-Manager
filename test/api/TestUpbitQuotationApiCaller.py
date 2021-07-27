import unittest

from main.api.UpbitQuotationApiCaller import UpbitQuotationApiCaller


class TestUpbitQuotationApiCaller(unittest.TestCase):
    def setUp(self):
        self.api_caller = UpbitQuotationApiCaller()

    def test_get_minutes_candle(self):
        candles = self.api_caller.get_candles("KRW-BTC", 1, "minutes/1")
        candle = candles[0]

        response_list = [
            "market",
            "candle_date_time_utc",
            "candle_date_time_kst",
            "opening_price",
            "high_price",
            "low_price",
            "trade_price",
            "timestamp",
            "candle_acc_trade_price",
            "candle_acc_trade_volume",
            "unit",
        ]

        for response_key in response_list:
            self.assertTrue(
                response_key in candle, f"{response_key} is not in candle: {candle}"
            )

        for response_key in candle:
            self.assertTrue(
                response_key in response_list,
                f"{response_key} is not in response_list: {response_list}",
            )

    def test_get_days_candle(self):
        candles = self.api_caller.get_candles("KRW-BTC", 1, unit="days")
        candle = candles[0]

        response_list = [
            "market",
            "candle_date_time_utc",
            "candle_date_time_kst",
            "opening_price",
            "high_price",
            "low_price",
            "trade_price",
            "timestamp",
            "candle_acc_trade_price",
            "candle_acc_trade_volume",
            "prev_closing_price",
            "change_price",
            "change_rate",
        ]

        for response_key in response_list:
            self.assertTrue(
                response_key in candle, f"{response_key} is not in candle: {candle}"
            )

        for response_key in candle:
            self.assertTrue(
                response_key in response_list,
                f"{response_key} is not in response_list: {response_list}",
            )

    def test_get_weeks_candle(self):
        candles = self.api_caller.get_candles("KRW-BTC", 1, unit="weeks")
        candle = candles[0]

        response_list = [
            "market",
            "candle_date_time_utc",
            "candle_date_time_kst",
            "opening_price",
            "high_price",
            "low_price",
            "trade_price",
            "timestamp",
            "candle_acc_trade_price",
            "candle_acc_trade_volume",
            "first_day_of_period",
        ]

        for response_key in response_list:
            self.assertTrue(
                response_key in candle, f"{response_key} is not in candle: {candle}"
            )

        for response_key in candle:
            self.assertTrue(
                response_key in response_list,
                f"{response_key} is not in response_list: {response_list}",
            )

    def test_get_months_candle(self):
        candles = self.api_caller.get_candles("KRW-BTC", 1, unit="months")
        candle = candles[0]

        response_list = [
            "market",
            "candle_date_time_utc",
            "candle_date_time_kst",
            "opening_price",
            "high_price",
            "low_price",
            "trade_price",
            "timestamp",
            "candle_acc_trade_price",
            "candle_acc_trade_volume",
            "first_day_of_period",
        ]

        for response_key in response_list:
            self.assertTrue(
                response_key in candle, f"{response_key} is not in candle: {candle}"
            )

        for response_key in candle:
            self.assertTrue(
                response_key in response_list,
                f"{response_key} is not in response_list: {response_list}",
            )


if __name__ == "__main__":
    unittest.main()
