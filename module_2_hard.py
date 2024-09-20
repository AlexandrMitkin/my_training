# import random
# b1 = int(random.uniform(3, 20.1))
a1 = 0
while (a1 < 3 or a1 > 20):
    a1 = int(input("введите число от 3 до 20 "))
    if a1 < 3 or a1 > 20:
        print("число вне диапазона, надо заново")
# print(a1," ",b1)
a2 = ""
for i in range(1, a1 // 2 + 1):
    for j in range(i + 1, a1 + 1 - i):
        if a1 % (i + j) == 0:
            a2 = a2 + str(i) + str(j)
print(a1, " ", a2)
