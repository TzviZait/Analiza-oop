from rectangie import Rectangle
from square import Square
from triangle import Triangle
from circle import Circle
from hexagon import Hexagon


def main():
    try:
        shapes = [
            Rectangle(5,10),
            Square(10),
            Triangle(3,4),
            Circle(5),
            Hexagon(5)
        ]

        for shape in shapes:
             print(shape)

    except (TypeError, ValueError) as e:
        print(e)

if __name__ == "__main__":
    main()