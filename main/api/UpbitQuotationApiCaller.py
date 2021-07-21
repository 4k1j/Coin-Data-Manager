import requests

from api.ApiCaller import ApiCaller


class UpbitQuotationApiCaller(ApiCaller):
    def __init__(self):
        super().__init__()

    def request(self, url: str, params: dict, method="GET"):
        url = self.server_url + url
        headers = {"accept": "application/json"}

        return requests.request(method, url, params=params, headers=headers).json()

    def get_market_code(self):
        url = "/v1/market/all"
        query = {"isDetails": "true"}
        return self.request(url, query)

    def get_candle(self, market, count, unit="minutes/1", to=None):
        if count > 200:
            raise Exception(f"Count can't exceed 200 : {200}")

        url = "/v1/candles/" + unit
        query = {"market": market, "count": count}
        return self.request(url, query)

