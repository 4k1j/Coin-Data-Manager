from abc import ABCMeta, abstractmethod
from typing import List

from main.candle.Candle import Candle


class CandleCaller(metaclass=ABCMeta):

    @abstractmethod
    def get_candles(self, market, count, unit, to=None) -> List[Candle]:
        pass
