def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        if first != 0:
            return first
        else:
            return 1


s = get_multiplied_digits(input("ведите число "))
print(s)