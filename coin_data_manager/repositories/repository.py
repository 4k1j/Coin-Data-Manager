import abc
from typing import List


class AlreadyExistError(Exception):
    pass

class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, model):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, model):
        raise NotImplementedError

    @abc.abstractmethod
    def get_all(self) -> List:
        raise NotImplementedError

    @abc.abstractmethod
    def update(self, model):
        raise NotImplementedError

    @abc.abstractmethod
    def upsert(self, model):
        raise NotImplementedError
