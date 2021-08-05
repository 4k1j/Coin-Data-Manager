import jwt
import uuid
import hashlib
from urllib.parse import urlencode
import requests

from coin.api.ExchangeApiCaller import ExchangeApiCaller


class UpbitExchangeApiCaller(ExchangeApiCaller):
    def __init__(self, access_key, secret_key):
        self.access_key = access_key
        self.secret_key = secret_key
        self.server_url = "https://api.upbit.com/v1"

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

    def request(self, request_url, params: dict = None, method="GET"):
        authorization_token = self._get_authorization_token(query=params)
        headers = {"Authorization": authorization_token}

        request_args = {"headers": headers}

        if params is not None:
            request_args["params"] = params

        return requests.request(
            method, self.server_url + request_url, **request_args
        ).json()

    def get_orders_chance(self, market):
        query = {"market": market}
        return self.request("/orders/chance", query)

    def get_accounts(self):
        return self.request("/accounts")
