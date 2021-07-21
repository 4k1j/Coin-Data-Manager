import requests

from main.api.ApiCaller import ApiCaller


class UpbitQuotationApiCaller(ApiCaller):
    def __init__(self):
        super().__init__()

    def request(self, url: str, params: dict, method="GET"):
        url = self.server_url + url
        headers = {"Accept": "application/json"}

        return requests.request(method, url, params=params, headers=headers).json()

    def get_market_code(self):
        url = "/market/all"
        query = {"isDetails": "true"}
        return self.request(url, query)

    def get_candle(self, market, count, unit="minutes/1", to=None):
        """
        :param market: Market code ex) KRW-BTC
        :param count: Quantity you want to receive
        :param unit: Unit of minutes ex) 1, 3, 5, 10, 15, 30, 60, 240
        :param to: Last candle time like yyyy-MM-dd'T'HH:mm:ss'Z' or yyyy-MM-dd HH:mm:ss
        :return: candles json data
        """
        if count > 200:
            raise Exception(f"Count can't exceed 200 : {200}")

        url = "/candles/" + unit
        query = {"market": market, "count": count}

        if to is not None:
            query["to"] = to

        return self.request(url, query)

    def get_ticker(self, markets):
        url = "/ticker"
        query_string = {"markets": markets}

        return self.request(url=url, params=query_string)
