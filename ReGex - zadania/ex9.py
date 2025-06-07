import re

class Solution:
    @staticmethod
    def check(text):

        pattern = r"(,$)|(\d{1}-)"
        res = re.search(pattern = pattern, string = text)
        if res:
            print(f"{text} is invalid")

def main():

    texts = ["123,2341515132135", "-10", "18-12", "123,"]
    func = Solution.check
    [func(text) for text in texts]

if __name__ == "__main__":
    main()