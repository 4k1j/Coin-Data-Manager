from abc import ABCMeta, abstractmethod


class ExchangeApiCaller(metaclass=ABCMeta):

    @abstractmethod
    def get_accounts(self) -> dict:
        pass
