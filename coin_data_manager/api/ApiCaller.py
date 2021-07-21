from abc import ABCMeta, abstractmethod


class ApiCaller(metaclass=ABCMeta):

    @abstractmethod
    def get_candles(self, market: str, count: int, unit: str):
        pass

    @abstractmethod
    def get_ticker(self, markets):
        pass
