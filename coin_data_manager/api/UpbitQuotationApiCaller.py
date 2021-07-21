from typing import List

import requests

from coin_data_manager.api.ApiCaller import ApiCaller
from coin_data_manager.model.candle import Candle


class UpbitQuotationApiCaller(ApiCaller):
    def __init__(self):
        self.server_url = "https://api.upbit.com/v1"

    def request(self, url: str, params: dict, method="GET"):
        url = self.server_url + url
        headers = {"Accept": "application/json"}

        return requests.request(method, url, params=params, headers=headers).json()

    def get_market_codes(self):
        url = "/market/all"
        query = {"isDetails": "true"}
        return self.request(url, query)

    # TODO unit to enum
    def get_candles(self, market: str, count: int, unit: str, to=None) -> List[Candle]:
        """
        :param market: Market code ex) KRW-BTC
        :param count: Quantity you want to receive
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

        url = "/candles/" + unit
        query = {"market": market, "count": count}

        if to is not None:
            query["to"] = to

        response = self.request(url, query)
        candles = [
            Candle.from_response(candle_info, unit) for candle_info in response
        ]

        return candles

    def get_ticker(self, markets):
        url = "/ticker"
        query_string = {"markets": markets}

        return self.request(url=url, params=query_string)
