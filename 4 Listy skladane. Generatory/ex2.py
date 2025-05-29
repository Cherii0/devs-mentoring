

class Generator:

    def __init__(self, n):
        self.prime_numbers = [1]
        self.upper_boundary = n

    @staticmethod
    def check_prime_number(n):
        for i in range(2, n):
            if n % i == 0:
                return None
            else:
                pass
        return n

    def generate(self):
        for i in range(2, self.upper_boundary + 1):
            res = Generator.check_prime_number(i)
            if res:
                yield i


    def testing(self):
        for i in range(2, self.upper_boundary + 1):
            yield i


    def show_prime_numbers(self):
        print(self.prime_numbers)

def main():
    generator = Generator(n=97)
    gen = generator.generate()
    print(next(gen))
    print(next(gen))
    print(next(gen))
    generator.show_prime_numbers()

if __name__ == "__main__":
    main()
