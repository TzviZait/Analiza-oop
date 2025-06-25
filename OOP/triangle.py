import math

from OOP.rectangie import Rectangle


class Triangle(Rectangle):
    def __init__(self, length, width):
        super().__init__(length, width)
        self.name = "Triangle"

    def get_area(self):
        return Rectangle(self.length,self.width).get_area() / 2

    def get_scope(self):
        return self.width + self.length + math.sqrt(self.length**2 + self.width**2)

