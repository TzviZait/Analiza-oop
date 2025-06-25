from area_Calculator import Shape


class Square(Shape):
    def __init__(self,side):
        if not isinstance(side, (int, float)):
            raise TypeError("The side must be a number.")
        if side <= 0:
            raise ValueError("The side must be positive.")
        self.side = side

    def get_area(self):
        return self.side * self.side

    def get_scope(self):
        return self.side * 4