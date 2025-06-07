import re

class Solution:
    @staticmethod
    def check(text):
        pattern = "(?P<username>[a-z]{1,})(@)(?P<company>[a-z]{1,})(.)(com)"
        username, company = re.match(pattern = pattern, string = text, flags = re.I).group("username", "company")
        return company


def main():

    texts = ["username@companyname.com"]
    func = Solution.check
    print(*[func(text) for text in texts])

if __name__ == "__main__":
    main()