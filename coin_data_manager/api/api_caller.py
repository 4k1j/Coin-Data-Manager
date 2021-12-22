from abc import ABCMeta, abstractmethod
from datetime import datetime
from typing import List

import requests
from coin_data_manager.models.candle import Candle
from coin_data_manager.util import CandleUnit, TooManyRequestsError


class ApiCaller(metaclass=ABCMeta):

    @abstractmethod
    def get_candles(self, market: str, count: int, unit: CandleUnit):
        pass

    @abstractmethod
    def get_ticker(self, markets):
        pass


class SimpleApiCaller(ApiCaller):

    def get_ticker(self, markets):
        pass

    def get_candles(self, market: str, count: int, unit: CandleUnit):
        return [Candle(market, unit, datetime.now(), 0, 0, 0, 0) for _ in range(count)]


class UpbitApiCaller(ApiCaller):
    def __init__(self):
        self.server_url = "https://api.upbit.com/v1"

    def _request(self, url: str, params: dict, method="GET"):
        url = self.server_url + url
        headers = {"Accept": "application/json"}

        response = requests.request(method, url, params=params, headers=headers)

        if response.status_code == 429 and "Too many API requests" in response.text:
            raise TooManyRequestsError(f"Too many requests with {url}, {params}")

        return response.json()

    def get_market_codes(self):
        url = "/market/all"
        query = {"isDetails": "true"}
        return self._request(url, query)

    def get_candles(self, market: str, count: int, unit: CandleUnit, to=None) -> List[Candle]:
        """
        :param market: Market code ex) KRW-BTC
        :param count: Quantity you want to receive 1 ~ 200
        :param unit: Candle unit
                ex) - minutes /1, /3, /5, /10, /15, /30, /60, /240
                    - days
                    - weeks
                    - months
        :param to: Last candle time like yyyy-MM-dd'T'HH:mm:ss'Z' or yyyy-MM-dd HH:mm:ss
        :return: candles json data
        """
        if count > 200:
            raise Exception(f"Count can't exceed 200 : {200}")

        url = "/candles/" + unit.value
        query = {"market": market, "count": count}

        if to is not None:
            query["to"] = to

        response = self._request(url, query)
        candles = [
            Candle.from_response(candle_info, unit) for candle_info in response
        ]

        return candles

    def get_ticker(self, markets):
        url = "/ticker"
        query_string = {"markets": markets}

        return self._request(url=url, params=query_string)

    def get_price(self, market):
        return self.get_ticker(market)[0]["trade_price"]
