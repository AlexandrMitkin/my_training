def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(2)
print_params(2, 3)
print_params(2, 3, False)
print_params(2, 3, "Fals")
print_params(b=25)
print_params(c=[1, 2, 3])
print("часть 2")
values_list = [2, "fg", False]
values_dict = {"c": 3, "b": "as", "a": False}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = ["ffff", True]
print_params(*values_list_2, 42)

