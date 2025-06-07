import re

class Solution:
    @staticmethod
    def check(text):

        pattern = r"(?P<date>.{1,})(:)(?P<temp>.{1,})"
        res = re.match(pattern = pattern, string = text).group("date")
        print(res)

def main():

    texts = ["2019-03-11: 23.5",
             "19/03/12: 12.7",
             "2019.03.13: 11.1",
             "2019-marzec-14: 14.3"]
    func = Solution.check
    [func(text) for text in texts]

if __name__ == "__main__":
    main()