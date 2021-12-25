class Candle:
    def __init__(
        self,
        market,
        unit,
        _datetime,
        open_price,
        high_price,
        low_price,
        close_price,
        acc_trade_price,
        acc_trade_volume,
    ):
        self.market = market
        self.unit = unit
        self.datetime = _datetime
        self.open_price = open_price
        self.high_price = high_price
        self.low_price = low_price
        self.close_price = close_price
        self.acc_trade_price = acc_trade_price
        self.acc_trade_volume = acc_trade_volume

    def __repr__(self):
        return f"{self.market} {self.datetime} {self.close_price}"

    @staticmethod
    def from_response(response: dict, unit):
        try:
            market = response["market"]
            candle_date_time_utc = response["candle_date_time_utc"]
            open_price = response["opening_price"]
            high_price = response["high_price"]
            low_price = response["low_price"]
            close_price = response["trade_price"]
            acc_trade_price = response["candle_acc_trade_price"]
            acc_trade_volume = response["candle_acc_trade_volume"]
        except Exception as e:
            print(response)
            raise e

        return Candle(
            market,
            unit.value,
            candle_date_time_utc,
            open_price,
            high_price,
            low_price,
            close_price,
            acc_trade_price,
            acc_trade_volume,
        )