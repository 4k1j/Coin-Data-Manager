class Candle:
    def __init__(
        self, market, date_time_utc, opening_price, high_price, low_price, last_price
    ):
        self.market = market
        self.time_utc = date_time_utc
        self.opening_price = opening_price
        self.high_price = high_price
        self.low_price = low_price
        self.last_price = last_price

