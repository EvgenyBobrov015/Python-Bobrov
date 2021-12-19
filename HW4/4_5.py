from functools import reduce


def my_func(el1, el2):
    return el1 * el2


print(reduce(my_func, [n for n in range(100, 1001, 2)]))
