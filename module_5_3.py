from module_5_1_2 import House


class ChildH(House):
    def __new__(cls):
        pass
    #def __eq__(self, other):
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

    #def __add__(self, value):
        #sc = value if isinstance(value, int) else value.number_of_floors
        #self.number_of_floors = self.number_of_floors + sc
        #print(type(self.number_of_floors)) #self.number_of_floors
        #return self

    def __radd__(self, value):
        return self + value

    def __iadd__(self, value):
        self.number_of_floors += value
        return self


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)  # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

# h1 += 10 # __iadd__
print(h1)

# h2 = 10 + h2 # __radd__
print(h2)

# print(h1 > h2) # __gt__
# print(h1 >= h2) # __ge__
# print(h1 < h2) # __lt__
# print(h1 <= h2) # __le__
print(h1 != h2)  # __ne__
