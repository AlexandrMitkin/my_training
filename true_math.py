from math import inf


def divide(first, second):
    if second == 0:
        if first>0:
            return inf
        elif first<0:
            return -inf
        return "misunderstanding"
    else:
        return first / second
