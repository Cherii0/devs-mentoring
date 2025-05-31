import time
from functools import reduce


class Timethis:
    dict_func = dict()

    # cannot be classmethod because we need separate objects for each decorated function
    def __init__(self, func):
        Timethis.dict_func.update({self : func.__name__})
        self.func = func
        self.measurements = []
        self.start = 0
        self.end = 0

    def __call__(self, **kwargs):
        """
        measure time decorated function and appends result into bin
        """
        self.start = time.time()
        self.func(file_path=kwargs.get("file_path"), saving_path=kwargs.get("saving_path"), word=kwargs.get("word"))
        self.end = time.time()
        self.measurement = self.end - self.start

        self.measurements.append(round(self.measurement, 2))

    def __str__(self):
        measurements_num = len(self.measurements)
        measurements_sum = reduce(lambda total, s : total + s, self.measurements)
        return str(measurements_sum / measurements_num)

    def name(self):
        return Timethis.dict_func.get(self)

    name = property(fget = name)


@Timethis
def reverse_file(**kwargs) -> None:
    data = []
    reversed_data = []
    with open(file=kwargs["file_path"], mode="r", encoding="UTF-8") as file:
        data = file.readlines()

    for line in reversed(data):
        reversed_data.append(line)

    with open(file=kwargs["file_path"], mode="w", encoding="UTF-8") as file:
        for line in reversed_data:
            file.write(line)


@Timethis
def count_word(**kwargs):
    counter = 0
    words = []
    with open(file=kwargs.get("file_path"), mode="r", encoding="UTF-8") as file:
        lines = file.readlines()
        for line in lines:
            line_words = line.split(" ")
            formated_line_words = list(map(lambda word : word.replace("\n", ""), line_words))
            words.extend(formated_line_words)
    counter = words.count(kwargs.get("word"))

def main():

    reverse_file(file_path = "book.txt", saving_path = "reversed_book.txt")
    count_word(file_path = "book.txt", word = "the")
    print(f"average execution time {reverse_file} for function {reverse_file.name}")
    print(f"average execution time {count_word} for function {count_word.name}")


if __name__ == "__main__":
    main()
