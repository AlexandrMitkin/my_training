def add_everything_up(a, b):
    try:
        s = a + b
    except:
        s = str(a) + str(b)
    return s


def add_everything_up2(a, b):
    try:
        if not isinstance(a, int):
            a = float(a)
        else:
            a = int(a)
        if not isinstance(b, int):
            b = float(b)
        else:
            b = int(b)
        s = a + b

        if isinstance(s, float):
            # s=str(s)
            # print("s= ",str(s))
            s = "{0:.3f}".format(s)
    except:
        s = str(a) + str(b)
    return s


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
# a=123.456
# b=7
# print(float("{0:.3f}".format(a+b)))

a = input("Enter a ")
b = input("Enter b ")
print(add_everything_up2(a, b))
