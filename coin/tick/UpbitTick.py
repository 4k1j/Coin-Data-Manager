from coin.tick.Tick import Tick


class UpbitTick(Tick):
    def __init__(
        self,
        market,
        trade_date_utc,
        trade_time_utc,
        timestamp,
        trade_price,
        trade_volume,
        prev_closing_price,
        change_price,
        ask_bid,
        sequential_id,
    ):
        super().__init__(
            market, timestamp, trade_price, trade_volume, change_price, ask_bid
        )
        self.trade_date_utc = trade_date_utc
        self.trade_time_time = trade_time_utc
        self.prev_closing_price = prev_closing_price
        self.sequential_id = sequential_id

    @staticmethod
    def from_response(market, response: dict):
        trade_date_utc = response["trade_date_utc"]
        trade_time_utc = response["trade_time_utc"]
        timestamp = response["timestamp"]
        trade_price = response["trade_price"]
        trade_volume = response["trade_volume"]
        prev_closing_price = response["prev_closing_price"]
        change_price = response["change_price"]
        ask_bid = response["ask_bid"]
        sequential_id = response["sequential_id"]

        return UpbitTick(
            market,
            trade_date_utc,
            trade_time_utc,
            timestamp,
            trade_price,
            trade_volume,
            prev_closing_price,
            change_price,
            ask_bid,
            sequential_id,
        )
