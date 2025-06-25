import math

from area_Calculator import Shape


class Hexagon(Shape):
    def __init__(self,rib):
        if not isinstance(rib, (int, float)):
            raise TypeError("The rib must be a number.")
        if rib <= 0:
            raise ValueError("The rib must be positive.")
        self.rib = rib

    def get_area(self):
        return (3 * math.sqrt(3) * self.rib ** 2) / 2

    def get_scope(self):
        return self.rib * 6

