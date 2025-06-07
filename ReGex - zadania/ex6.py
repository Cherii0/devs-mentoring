import re

class Solution:
    @staticmethod
    def check(text):
        pattern = "(<.{0,}?>)(.{0,}?)(<\/.{0,}?>)"
        gr2 = re.match(pattern = pattern, string = text, flags = 0)
        return gr2


def main():

    texts = ["<span>Yowza! That’s a great regular expression.</span>",
             "<p>You\'re going to love them!</p> <p>Learn about regular expressions here.</p> "]

    func = Solution.check
    print(*[func(text) for text in texts])

if __name__ == "__main__":
    main()