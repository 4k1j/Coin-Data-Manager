from coin.api.UpbitExchangeApiCaller import UpbitExchangeApiCaller
from coin.api.UpbitQuotationApiCaller import UpbitQuotationApiCaller
from coin.bot.TraidingBot import TradingBot


class UpbitTradingBot(TradingBot):
    def __init__(
            self,
            exchange_api: UpbitExchangeApiCaller,
            quotation_api: UpbitQuotationApiCaller,
    ):
        self.exchange_api = exchange_api
        self.quotation_api = quotation_api

    def sell_coin(self):
        pass

    def buy_coin(self):
        pass


