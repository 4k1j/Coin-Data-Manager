from coin.api.UpbitExchangeApiCaller import UpbitExchangeApiCaller
from coin.api.UpbitQuotationApiCaller import UpbitQuotationApiCaller
from coin.bot.Prediction import Prediction
from coin.bot.TraidingBot import TradingBot


class UpbitTradingBot(TradingBot):
    def __init__(
            self,
            exchange_api: UpbitExchangeApiCaller,
            quotation_api: UpbitQuotationApiCaller,
            cycle: int
    ):
        super().__init__(exchange_api, quotation_api, cycle)

    def buy_coin(self):
        pass

    def sell_coin(self):
        pass

    def predict(self) -> Prediction:
        pass


