from abc import abstractmethod


class ModelRepMixin:
    @abstractmethod
    def to_pretty(self):
        pass
