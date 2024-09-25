class House:
    def __init__(self, name1, number_of_floors1):
        self.name = name1
        self.number_of_floors = number_of_floors1

    def go_to(self, new_floor1):
        new_floor = new_floor1
        if new_floor < 1 or new_floor > self.number_of_floors:
            print("there is no such floor")
            return
        for i in range(1, new_floor + 1):
            print(i)


nhouse = input("enter the name of the house ")
fhouse = int(input("enter the number floos in the house "))

House1 = House(nhouse, fhouse)

gflouse = int(input("enter the floor where you would like to go up "))
House1.go_to(gflouse)
