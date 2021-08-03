from abc import ABCMeta, abstractmethod


class TradingBot(metaclass=ABCMeta):

    @abstractmethod
    def buy_coin(self):
        pass

    @abstractmethod
    def sell_coin(self):
        pass


