from abc import abstractmethod


class Shape:

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_scope(self):
        pass
