import jwt
import uuid
import hashlib
from urllib.parse import urlencode
import requests

from main.api.ApiCaller import ApiCaller


class UpbitExchangeApiCaller(ApiCaller):
    def __init__(self, access_key, secret_key):
        super().__init__()
        self.access_key = access_key
        self.secret_key = secret_key

    @staticmethod
    def _get_query_hash(query):
        m = hashlib.sha512()
        m.update(urlencode(query).encode())
        return m.hexdigest()

    def _get_authorization_token(self, query=None, query_hash_alg="SHA512"):
        payload = {
            "access_key": self.access_key,
            "nonce": str(uuid.uuid4()),
        }

        if query is not None:
            payload["query_hash"] = self._get_query_hash(query)
            payload["query_hash_alg"] = query_hash_alg

        jwt_token = jwt.encode(payload, self.secret_key)
        return f"Bearer {jwt_token}"

    def request(self, url, params: dict, method="GET"):
        authorization_token = self._get_authorization_token(params)
        headers = {"Authorization": authorization_token}

        return requests.request(method, self.server_url + url, params=params, headers=headers).json()

    def get_orders_chance(self, market):
        query = {"market": market}
        return self.request("/v1/orders/chance", query)
