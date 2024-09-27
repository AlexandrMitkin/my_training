#from module_5_1_2 import House
#from module_5_3 import ChildH


#class House2(ChildH, House):
class House2():
    houses_history = []
    ss = ""

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, name1, number_of_floors1):
        self.name = name1
        self.number_of_floors = number_of_floors1

    def __del__(self):
        if House2.ss == "":
            print(f"{self.name} снесён, но он останется в истории")


h1 = House2('ЖК Эльбрус', 10)
print(House2.houses_history)
h2 = House2('ЖК Акация', 20)
print(House2.houses_history)
h3 = House2('ЖК Матрёшки', 20)
print(House2.houses_history)

del h2
del h3

print(House2.houses_history)

input()
House2.ss = " "
