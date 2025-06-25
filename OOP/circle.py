import math

from area_Calculator import Shape


class Circle(Shape):
    def __init__(self,radius):
        if not isinstance(radius, (int, float)):
            raise TypeError("The radius must be a number.")
        if radius <= 0:
            raise ValueError("The radius must be positive.")
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2

    def get_scope(self):
        return 2 * math.pi * self.radius


