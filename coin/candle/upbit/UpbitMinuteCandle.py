from coin.candle.Candle import Candle


class UpbitMinuteCandle(Candle):
    def __init__(
        self,
        market,
        candle_date_time_utc,
        candle_date_time_kst,
        opening_price,
        high_price,
        low_price,
        trade_price,
        timestamp,
        candle_acc_trade_price,
        candle_acc_trade_volume,
        unit,
    ):
        super().__init__(
            market,
            candle_date_time_utc,
            opening_price,
            high_price,
            low_price,
            trade_price,
        )
        self.candle_date_time_kst = candle_date_time_kst
        self.timestamp = timestamp
        self.candle_acc_trade_price = candle_acc_trade_price
        self.candle_acc_trade_volume = candle_acc_trade_volume
        self.unit = unit

    @staticmethod
    def from_response(response: dict):
        market = response["market"]
        candle_date_time_utc = response["candle_date_time_utc"]
        candle_date_time_kst = response["candle_date_time_kst"]
        opening_price = response["opening_price"]
        high_price = response["high_price"]
        low_price = response["low_price"]
        trade_price = response["trade_price"]
        timestamp = response["timestamp"]
        candle_acc_trade_price = response["candle_acc_trade_price"]
        candle_acc_trade_volume = response["candle_acc_trade_volume"]
        unit = response["unit"]

        return UpbitMinuteCandle(
            market,
            candle_date_time_utc,
            candle_date_time_kst,
            opening_price,
            high_price,
            low_price,
            trade_price,
            timestamp,
            candle_acc_trade_price,
            candle_acc_trade_volume,
            unit,
        )
