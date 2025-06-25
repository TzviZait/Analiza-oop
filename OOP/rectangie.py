from area_Calculator import Shape


class Rectangle(Shape):
    def __init__(self,length,width):
        if not isinstance(length, (int, float)):
            raise TypeError("The length must be a number.")
        if length <= 0:
            raise ValueError("The length must be positive.")
        if not isinstance(width, (int, float)):
            raise TypeError("The width must be a number.")
        if width <= 0:
            raise ValueError("The width must be positive.")
        self.length = length
        self.width = width

    def get_area(self):
        return self.width * self.length

    def get_scope(self):
        return self.width * 2 + self.length *2

