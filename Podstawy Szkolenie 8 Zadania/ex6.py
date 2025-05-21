

class Solution:

    def __init__(self):
        self.line_num = 4
        self.desired_line = ""
        self.raw_lines = []
        self.line = "..."
        self.counter = 0

    # approach 1
    def read_file(self, filename):
        with open(filename, "r") as file:
            self.raw_lines.extend(file.readlines())

        self.desired_line = self.raw_lines[self.line_num - 1]

    # approach 2
    def read_file2(self, filename):
        with open(filename, "r") as file:

            while self.line != "":
                self.line = file.readline()
                if self.counter == 3:
                    self.desired_line = self.line
                    break
                self.counter += 1



    def show_result(self):
        print(self.desired_line)


def main():
    solution = Solution()
    solution.read_file("test.txt")
    solution.read_file2("test.txt")
    solution.show_result()

if __name__ == "__main__":
    main()
