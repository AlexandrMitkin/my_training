class Animal:
    alive = True

    def __init__(self, name1, fed1=False):
        self.name = name1
        self.fed = fed1


class Plant:
    edible_M = False
    edible_P = False

    def __init__(self, name1):
        self.name = name1


class Mammal(Animal):
    def __init__(self, name1, fed1=False):
        self.name = name1
        self.fed = fed1
        self.alive = Animal.alive

    def eat(self, food1):
        if isinstance(food1, Fruit):
            if Fruit.edible_M == True:
                print(f"{self.name} съел {food1.name}")
                self.fed = True
            else:
                print(f"{self.name} не стал есть {food1.name}")
                self.alive = False
        elif isinstance(food1, Flower):
            if Flower.edible_M == True:
                print(f"{self.name} съел {food1.name}")
                self.fed = True
            else:
                print(f"{self.name} не стал есть {food1.name}")
                self.alive = False


class Predator(Animal):
    def __init__(self, name1, fed1=False):
        self.name = name1
        self.fed = fed1
        self.alive = Animal.alive

    def eat(self, food1):
        if isinstance(food1, Fruit):
            if Fruit.edible_P == True:
                print(f"{self.name} съел {food1.name}")
                self.fed = True
            else:
                print(f"{self.name} не стал есть {food1.name}")
                self.alive = False
        elif isinstance(food1, Flower):
            if Flower.edible_P == True:
                print(f"{self.name} съел {food1.name}")
                self.fed = True
            else:
                print(f"{self.name} не стал есть {food1.name}")
                self.alive = False


class Flower(Plant):
    edible_M = Plant.edible_M
    edible_P = Plant.edible_P

    def __init__(self, name1, edible_M1=Plant.edible_M, edible_P1=Plant.edible_P):
        self.name = name1
        Flower.edible_M = edible_M1
        Flower.edible_P = edible_P1


class Fruit(Plant):
    edible_M = Plant.edible_M
    edible_P = Plant.edible_P

    def __init__(self, name1, edible_M1=True, edible_P1=Plant.edible_P):
        self.name = name1
        # self.edible_M = edible_M1
        # self.edible_P = edible_P1
        Fruit.edible_M = edible_M1
        Fruit.edible_P = edible_P1


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
