from module_5_1_2 import House


class ChildH(House):
    def __init__(self, name1, number_of_floors1):
        self.name = name1
        self.number_of_floors = number_of_floors1

    def __lt__(self, other):
        # return self.number_of_floors < other.number_of_floors
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors < other

    def __le__(self, other):
        return House.__eq__(self, other) or self.__lt__(other)

    def __gt__(self, other):
        return not self.__le__(other)

    def __ge__(self, other):
        return not self.__lt__(other)

    def __ne__(self, other):
        return not House.__eq__(self, other)

    def __radd__(self, value):
        return House.__add__(self, value)

    def __iadd__(self, value):
        return House.__add__(self, value)


h1 = ChildH('ЖК Эльбрус', 10)
h2 = ChildH('ЖК Акация', 20)
h3 = House('ЖК Эльбрус2', 30)
h4 = ChildH('ЖК Акация2', 40)

print(h1)
print(h2)
print(h3)
print(h4)

print(h1 == h2)  # __eq__
print(h3 == h2)

h1 = h1 + 10  # __add__
h3 = h3 + 10
print(h1)
print(h3)
print(h1 == h2)
print(h3 == h4)

print()
h1 += 10  # __iadd__
print(h1)

h2 = 10 + h2  # __radd__
print(h2)

print(h1 > h2)  # __gt__
print(h1 >= h2)  # __ge__
print(h1 < h2)  # __lt__
print(h1 <= h2)  # __le__
print(h1 != h2)  # __ne__

print(h1 > h2)  # __gt__
print(h1 >= h2)  # __ge__
print(h1 < h2)  # __lt__
print(h1 <= h2)  # __le__
print(h1 != h2)  # __ne__
