class Candle:
    def __init__(
        self, market, unit, _datetime, open_price, high_price, low_price, last_price
    ):
        self.market = market
        self.unit = unit
        self.datetime = _datetime
        self.open_price = open_price
        self.high_price = high_price
        self.low_price = low_price
        self.last_price = last_price

    def __repr__(self):
        return f"{self.market} {self.datetime} {self.last_price}"

    @staticmethod
    def from_response(response: dict, unit):
        market = response["market"]
        candle_date_time_utc = response["candle_date_time_utc"]
        open_price = response["opening_price"]
        high_price = response["high_price"]
        low_price = response["low_price"]
        trade_price = response["trade_price"]

        return Candle(
            market,
            unit,
            candle_date_time_utc,
            open_price,
            high_price,
            low_price,
            trade_price
        )
