def apply_all_func(int_list, *functions):
    results = {}
    for fun in functions:
        try:
            result = list(map(fun, int_list))
        except:
            result = list(map(fun, [int_list]))
        if len(result) == 1:
            result = result[0]
        results[fun.__name__] = result
    return results


# print(apply_all_func([6, 20, 15, 9], max, min), end="")
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
