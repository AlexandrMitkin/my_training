from module_5_1_2 import House


class ChildH(House):
    def __init__(self, name1, number_of_floors1):
        self.name = name1
        self.number_of_floors = number_of_floors1

    # def __eq__(self, other):
    #    if isinstance(other, int):
    #       return self.number_of_floors == other
    #  elif isinstance(other, House):
    #     return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    # def __add__(self, value):
    # sc = value if isinstance(value, int) else value.number_of_floors
    # self.number_of_floors = self.number_of_floors + sc
    # print(type(self.number_of_floors)) #self.number_of_floors
    # return self

    def __radd__(self, value):
        self.number_of_floors = self.number_of_floors + value

        return self

    def __iadd__(self, value):
        self.number_of_floors += value
        return self


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
