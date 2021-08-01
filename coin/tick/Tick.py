class Tick:
    def __init__(
            self,
            market,
            timestamp,
            trade_price,
            trade_volume,
            change_price,
            ask_bid,
    ):
        self.market = market
        self.timestamp = timestamp
        self.trade_price = trade_price
        self.trade_volume = trade_volume
        self.change_price = change_price
        self.ask_bid = ask_bid
