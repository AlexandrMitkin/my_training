class Animal:
    alive = True

    def __init__(self, name1, fed1=False):
        self.name = name1
        self.fed = fed1


class Plant:
    edible = False

    def __init__(self, name1):
        self.name = name1


class Mammal(Animal):
    def __init__(self, name1, fed1=False):
        self.name = name1
        self.fed = fed1
        self.alive = Animal.alive

    def eat(self, food1):
        if isinstance(food1, Plant):
            print(f"{self.name} съел {food1.name}")
            self.fed = True


class Predator(Animal):
    def __init__(self, name1, fed1=False):
        self.name = name1
        self.fed = fed1
        self.alive = Animal.alive

    def eat(self, food1):
        if isinstance(food1, Plant):
            print(f"{self.name} не стал есть {food1.name}")
            self.alive = False


class Flower(Plant):
    # edible1 = False
    edible = Plant.edible

    def __init__(self, name1):
        # global edible1
        self.name = name1
        self.edible1 = Plant.edible


class Fruit(Plant):
    edible = True

    def __init__(self, name1):
        self.name = name1
        # self.edible = True


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
