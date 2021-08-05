from abc import ABCMeta, abstractmethod
from typing import List

from coin.candle.Candle import Candle
from coin.tick.Tick import Tick
from coin.tick.Ticker import Ticker


class QuotationApiCaller(metaclass=ABCMeta):

    @abstractmethod
    def get_candles(self, market: str, count: int, unit: str, to=None) -> List[Candle]:
        pass

    @abstractmethod
    def get_ticks(self, market, count) -> List[Tick]:
        pass

    @abstractmethod
    def get_tickers(self, markets) -> List[Ticker]:
        pass
