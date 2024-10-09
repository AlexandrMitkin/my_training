def is_prime(func):
    def wrapper(a1, a2, a3):
        result = func(a1, a2, a3)
        if result == 1:
            print("numbe 1")
            return result
        if result == 2:
            print("simple")
            return result
        if result % 2 == 0:
            print("composite")
            return result
        i = 3
        while i < result / 2:
            if result % 3 == 0:
                print("composite")
                return result
            i += 2
        print("simple")
        return result

    return wrapper


@is_prime
def sum_three(a1, a2, a3):
    return a1 + a2 + a3


result = sum_three(2, 3, 6)
print(result)
