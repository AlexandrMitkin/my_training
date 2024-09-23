from fake_math import divide as divf
from true_math import divide as divt

while 1 > 0:
    s = input("enter any number or press 'Enter' ")
    if s == "":
        break
    print(divf(int(s),0))
    print(divt(int(s), 0))