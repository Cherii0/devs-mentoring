
class Solution:

    def __init__(self):
        self.data_raw = ""
        self.data_parsed = []
        self.data_to_write = ""

    def read_file(self, filename):
        with open(filename, "r", encoding="utf-8") as file:
            self.data_raw = file.read()

    def convert(self):
        self.data_parsed = self.data_raw.replace("\n", " ")
        self.data_parsed = self.data_parsed.split(" ")
        print(self.data_parsed)
        print(len(self.data_parsed))

        remove_elem = []

        for idx in range(0, len(self.data_parsed) - 1):
            curr_elem = self.data_parsed[idx]
            next_elem = self.data_parsed[idx + 1]
            if curr_elem == next_elem:
                remove_elem.append(self.data_parsed[idx])


        for word in self.data_parsed:
            if word in remove_elem:
                self.data_parsed.remove(word)

        for word in self.data_parsed:
            self.data_to_write += "".join(word)
            self.data_to_write += "".join(" ")

    def save_file(self, filename):

        with open(filename, "w") as file:
            file.write(self.data_to_write)


def main():
    solution = Solution()
    solution.read_file("przyklad.txt")
    solution.convert()
    solution.save_file("przyklad_poprawka.txt")

if __name__ == "__main__":
    main()

