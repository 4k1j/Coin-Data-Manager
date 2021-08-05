import time
from abc import ABCMeta, abstractmethod

from coin.api.ExchangeApiCaller import ExchangeApiCaller
from coin.api.QuotationApiCaller import QuotationApiCaller
from coin.bot.Prediction import Prediction


class TradingBot(metaclass=ABCMeta):

    def __init__(self, exchange_api_caller: ExchangeApiCaller, quotation_api_caller: QuotationApiCaller, cycle: int):
        self.cycle = cycle
        self.exchange_api_caller = exchange_api_caller
        self.quotation_api_caller = quotation_api_caller

    @abstractmethod
    def buy_coin(self):
        pass

    @abstractmethod
    def sell_coin(self):
        pass

    @abstractmethod
    def predict(self) -> Prediction:
        pass

    def run(self):
        while True:
            predict_result = self.predict()
            if predict_result == Prediction.UP:
                self.buy_coin()
            elif predict_result == Prediction.DOWN:
                self.sell_coin()

            time.sleep(self.cycle)



