
class Shape:

    def __init__(self, length):
        self.length = length

    def calculate_area(self):
        return 0

class Square(Shape):

    def __init__(self, length):
        super().__init__(length)

    def calculate_area(self):
        return self.length * self.length


def main():
    square1 = Square(50)
    square2 = Square(5)
    print(square1.calculate_area())
    print(square2.calculate_area())


if __name__ == '__main__':
    main()
