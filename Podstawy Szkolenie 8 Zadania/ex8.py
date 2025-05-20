import json


class Solution:

    def __init__(self):

        self.reversed_dict = {}


    def convert(self, **kwargs):

        for key, value in kwargs.items():
            self.reversed_dict.update({value: key})

    def save_result(self):
        with open("output.json", "w") as file:
            json.dump(self.reversed_dict, file, indent=4)


def main():
    program = Solution()
    program.convert(a = 1, b = 2, c = 3)
    program.save_result()

if __name__ == "__main__":
    main()
