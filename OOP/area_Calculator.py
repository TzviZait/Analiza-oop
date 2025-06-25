from abc import abstractmethod


class Shape:

    def __init__(self,name):
        self.name = name

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_scope(self):
        pass

    def __str__(self):
        return f"{self.name}: area: {self.get_area()} scope: {self.get_scope()}"