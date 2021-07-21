from abc import ABCMeta, abstractmethod


class ApiCaller(metaclass=ABCMeta):
    def __init__(self):
        self.server_url = "https://api.upbit.com/v1"

    @abstractmethod
    def request(self, url: str, params: dict, method="get"):
        pass

