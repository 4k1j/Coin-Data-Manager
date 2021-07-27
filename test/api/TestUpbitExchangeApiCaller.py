import unittest
from pathlib import Path

import yaml

from main.api.UpbitExchangeApiCaller import UpbitExchangeApiCaller


class TestUpbitExchangeApiCaller(unittest.TestCase):
    def setUp(self):

        with Path("api_key.yaml").open() as api_key_file:
            api_key = yaml.load(api_key_file, Loader=yaml.FullLoader)
            access_key = api_key["access_key"]
            secret_key = api_key["secret_key"]

            self.api_caller = UpbitExchangeApiCaller(
                access_key,
                secret_key
            )

    def test_get_accounts(self):
        accounts = self.api_caller.get_accounts()
        account = accounts[0]

        response_key_list = [
            "currency",
            "balance",
            "locked",
            "avg_buy_price",
            "avg_buy_price_modified",
            "unit_currency",
        ]

        for response_key in response_key_list:
            self.assertTrue(response_key in account)

        print(accounts)


if __name__ == "__main__":
    unittest.main()
