from module_5_1_1 import House

for i in range(1, 3):
    nhouse = input("enter the name of the house ")
    fhouse = int(input("enter the number floors in the house "))
    House2 = House(nhouse, fhouse)

    print()
    print("The length is equal to " + str(len(House2)))
    print(str(House2))
