
class Counter:
    func_dict = dict()

    @staticmethod
    def update_func(func):
        if func in Counter.func_dict.keys():
            Counter.func_dict[func]["counter"] += 1

    def __init__(self, func):
        # once called while assign decorator
        Counter.func_dict[self] = {"func_name" : func.__name__, "counter" : 0}

    def __call__(self):
        Counter.update_func(self)
        for value in Counter.func_dict.values():
            print(f"{value["func_name"]} : {value["counter"]}")


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
