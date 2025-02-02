from abc import ABC, abstractmethod


class IDataSource(ABC):
    @abstractmethod
    def get_biblia(self):
        pass

    def get_info_biblia(self):
        pass
