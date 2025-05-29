from random import randint, choices
from string import ascii_letters


class Generator:

    def __init__(self, iter_):
        self.iter_ = iter_

    def generate_random_value(self):
        value = None
        for i in range(self.iter_):
            match randint(1, 3):
                case 1:
                    value = choices(ascii_letters)
                case 2:
                    value = randint(1,100)
                case 3:
                    value = {randint(1, 100)}

            yield value
            # check for end of generator
            if i == self.iter_ - 1:
                self.generate_random_value().throw(IndexError("Generator ended iterations"))



def main():
    generator = Generator(3)
    gen = generator.generate_random_value()
    print(next(gen))
    print(next(gen))
    print(gen.__next__())
    # attempt to generate out of generator iterations
    print(gen.__next__())



if __name__ == "__main__":
    main()