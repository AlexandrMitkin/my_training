class Figure:
    sides_count = 0

    def __init__(self, filled1=False, color=[1, 1, 1], *args):
        self.filled = False
        self.color = color
        self.sides = list(args)
        if not isinstance(filled1, bool):
            self.sides = [self.color] + self.sides
            self.color = filled1
        else:
            self.filled = filled1
        if len(self.sides) != self.sides_count:
            self.sides = []
            for i in range(self.sides_count):
                self.sides += [1]
        self.__color = self.color
        self.__sides = self.sides

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        a = False
        if isinstance(r, int) and isinstance(g, int) and isinstance(b, int):
            if r >= 0 and g >= 0 and b >= 0:
                if r < 256 and g < 256 and b < 256:
                    a = True
        return a

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = r, g, b
            self.color = self.__color

    def __is_valid_sides(self, *args):
        a = False
        r = 0
        k = 0
        for i in args:
            k += 1
            if i < 0:
                r = 1
                break
        if r == 0 and k == len(self.__sides):
            a = True
        return a

    def get_sides(self):
        return self.__sides

    def __len__(Figure):
        s = 0
        for i in Figure.__sides:
            s += i
        return s

    def set_sides(self, *new_sides):
        k = 0
        for i in new_sides:
            k += 1
        if k == self.sides_count:
            self.__sides = [*new_sides]
            self.sides = self.__sides


class Circle(Figure):
    sides_count = 1

    def __init__(self, filled1, color=[255, 255, 255], *args):
        Figure.__init__(self, filled1, color, *args)

    def get_square(self):
        return self.__sides[0] * self.__radius / 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, filled1, color=[255, 255, 255], *args):
        Figure.__init__(self, filled1, color, *args)

    def get_square(self):
        a = Figure.__len__(self, self.__sides) / 2
        b = a * (a - self.__sides[0]) * (a - self.__sides[1]) * (a - self.__sides[2])
        return b ** 0.5


class Cube(Figure):
    sides_count = 12

    def __init__(self, filled1, color=[255, 255, 255], *args):
        if type(filled1) == bool:
            if len(color) + len(args) == 4:
                s = []
                for i in range(12):
                    s = s + [*args]
            else:
                s = [1]
        else:
            if len([color]) + len([*args]) == 1:
                s = []
                for i in range(11):
                    s = s + [color]
            else:
                s = [1]
        Figure.__init__(self, filled1, color, *s)

    def get_volume(self):
        return self.sides[0] ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
