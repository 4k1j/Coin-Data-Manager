class Candle:
    def __init__(
        self, market, unit, _datetime, opening_price, high_price, low_price, last_price
    ):
        self.market = market
        self.unit = unit
        self.datetime = _datetime
        self.opening_price = opening_price
        self.high_price = high_price
        self.low_price = low_price
        self.last_price = last_price

    @staticmethod
    def from_response(response: dict, unit):
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
        first_day_of_period = response["first_day_of_period"]

        return Candle(
            market,
            unit,
            candle_date_time_utc,
            opening_price,
            high_price,
            low_price,
            trade_price

        )
