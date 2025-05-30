from math import pow

class Solution:
    def __init__(self, source_list):
        self.source_list = source_list

    def get_converted_list(self, *, power):
        return list(map(lambda num : pow(num, power), self.source_list))


def main():
    source_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    solution = Solution(source_list)
    print(solution.get_converted_list(power = 1))
    print(solution.get_converted_list(power = 2))
    print(solution.get_converted_list(power = 3))

if __name__ == "__main__":
    main()