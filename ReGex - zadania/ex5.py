import re

class Solution:
    @staticmethod
    def check(text):
        pattern = r"(?!.*[aA])(?:[a-zA-Z]){6,}"
        return re.search(pattern = pattern, string = text, flags = re.I)



def main():
    texts = ["unique New York", "Regular Expressions", "ALOHA",
             "Python should match"]

    func = Solution.check
    print(*[func(text) for text in texts])

if __name__ == "__main__":
    main()