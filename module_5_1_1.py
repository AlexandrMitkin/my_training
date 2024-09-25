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

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"


def main1():
    nhouse = input("enter the name of the house ")
    fhouse = int(input("enter the number floors in the house "))

    House1 = House(nhouse, fhouse)

    gflouse = int(input("enter the floor where you would like to go up "))
    House1.go_to(gflouse)


if __name__ == "__main__":
    main1()
