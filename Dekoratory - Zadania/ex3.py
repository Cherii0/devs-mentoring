from functools import wraps


class Counter:
    func_dict = dict()

    @staticmethod
    def update_func(func):
        func = func.__ne__
        if func in Counter.func_dict.keys():
            Counter.func_dict[func] += 1
        else:
            Counter.func_dict[func] = 1

    @staticmethod
    def __init__(func):
        pass



    def __call__(self):
        Counter.update_func(self)
        for key, value in Counter.func_dict.items():
            print(f"{key} : {value}")


@Counter
def func1():
    pass

@Counter
def func2():
    pass

def main():

    func1()
    func1()

    func2()
    func2()
    func2()


if __name__ == "__main__":
    main()
