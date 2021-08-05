from coin.bot import TraidingBot

from abc import ABCMeta, abstractmethod


class BackTester(metaclass=ABCMeta):
    def __init__(self, trading_bot: TraidingBot):
        self.trading_bot = trading_bot

