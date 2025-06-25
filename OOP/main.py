from rectangie import Rectangle
from square import Square


def main():
    try:
        obj_rectangie = Rectangle(10,5)
        print(obj_rectangie.get_area())
        print(obj_rectangie.get_scope())

        obj_square = Square(10)
        print(obj_square.get_area())
        print(obj_square.get_scope())

    except (TypeError, ValueError) as e:
        print(e)

if __name__ == "__main__":
    main()