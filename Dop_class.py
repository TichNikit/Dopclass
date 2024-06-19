class Figure:
    sides_count = 0

    def __init__(self, __color, __sides):
        self.__sides = __sides
        self.__color = __color

    def get_color(self):
        return list(self.__color)

    def get_sides(self):
        return list(self.__sides)

    def __is_valid_color(self, r, g, h):
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= h <= 255:
            if isinstance(r, int) and isinstance(g, int) and isinstance(h, int):
                return True
            else:
                return False
        else:
            return False

    def set_color(self, r, g, h):
        if self.__is_valid_color(r, g, h):
            self.__color = [r, g, h]

    def set_sides(self, *sides):
        if self.__is_valid_sides(*sides):
            if isinstance(self, Cube):
                self._Cube__sides = [*sides]
                return self._Cube__sides
            else:
                self.__sides = [*sides]
        elif isinstance(self, Cube):
            return self._Cube__sides
        else:
            return self.__sides

    def __is_valid_sides(self, *count):
        check = [*count]
        if isinstance(self, Cube):
            check_old = self._Cube__sides
        else:
            check_old = [self.__sides]
        if len(check) == len(check_old):
            for i in check:
                if i < 0 or not isinstance(i, int):
                    return False
            else:
                return True
        else:
            return False

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __radius(self):
        return self.__sides / (2 * 3.14)

    def get_square(self):
        return self.__radius() ** 2 * 3.14


class Triangle(Figure):
    sides_count = 3

    def __height(self):
        height_ = [self.__sides]
        a = height_[0]
        b = height_[1]
        c = height_[2]
        p = (a + b + c) / 2
        return (2 * (p * (p - a) * (p - b) * (p - c)) ** (1 / 2)) / a

    def get_square(self):
        square = [self.__sides]
        a = square[0]
        return (self.__height() * a) / 2


class Cube(Figure):
    sides_count = 12

    def __init__(self, __color, __sides):
        super().__init__(__color, __sides)
        self.__sides = [__sides] * 12

    def get_volume(self):
        return self.__sides[0] ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)


circle1.set_color(55, 66, 77)  # Изменится
cube1.set_color(300, 70, 15)  # Не изменится
print(circle1.get_color())
print(cube1.get_color())

cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
circle1.set_sides(15)  # Изменится
print(cube1.set_sides())
print(circle1.set_sides())

print(len(circle1))

print(cube1.get_volume())
