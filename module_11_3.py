import sys
import inspect


class figa:
    def func2(self):
        pass


def func1():
    pass


def introspection_info(obj):
    info_dir = {}
    a = str(type(obj)).split(' ')[1]
    a = a[1:len(a) - 2]
    info_dir['тип'] = a

    print("атрибуты, методы, функции")
    print(dir(obj))
    print()

    print("методы:")
    print([arg for arg in dir(obj) if callable(getattr(obj, arg))])
    print()

    print("атрибуты:")
    print([arg for arg in dir(obj) if not callable(getattr(obj, arg))])
    print()

    # print([getattr(obj, arg) for arg in dir(obj) if not callable(getattr(obj, arg))])
    # print()

    # print(help(obj))

    a = inspect.getmodule(obj)
    if a == None:
        info_dir['модуль'] = "__main__"
    else:
        print(a)
    print()
    return info_dir


fig1 = figa()
# number_info = introspection_info(func1)
number_info = introspection_info(fig1)
print(number_info)
