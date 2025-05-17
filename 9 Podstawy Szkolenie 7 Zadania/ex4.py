from functools import reduce

def func(*args):
    res = reduce(lambda acc, x : acc*x, args)
    print(res)


func(1, 2, 3)
