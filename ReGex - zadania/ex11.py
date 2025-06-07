import re

class Solution:
    @staticmethod
    def check(text):

        pattern = r"(#[a-fA-F0-9]{3,3}$)|(#[a-fA-F0-9]{6,6}$)"
        res = re.search(pattern = pattern, string = text)
        if not res:
            print(f"{text}, is invalid")

def main():

    texts = ["#AB4B72",
             "#ab4",
             "#ab43",
             "#aaaaaaaaa",
             "ahl"]
    func = Solution.check
    [func(text) for text in texts]

if __name__ == "__main__":
    main()