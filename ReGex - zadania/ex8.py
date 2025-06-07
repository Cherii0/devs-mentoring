import re

class Solution:
    @staticmethod
    def check(text):
        pattern = r"(\d{1,})"
        res = re.findall(pattern = pattern, string = text)
        return res


def main():

    texts = ["2 cats and 3 dogs", "hej tutaj python 3 wersja z 2015"]
    func = Solution.check
    print(*[func(text) for text in texts])

if __name__ == "__main__":
    main()