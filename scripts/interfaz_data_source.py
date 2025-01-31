from abc import ABC, abstractmethod


class IDataSource(ABC):
    @abstractmethod
    def get_biblia_BLPH(self):
        pass
