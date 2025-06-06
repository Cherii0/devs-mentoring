
import re


class TextValidation:

    def __init__(self):
        pass

    @staticmethod
    def check(text):

        match = re.findall(pattern ="[a-z]_[a-z]", string = text, flags=0)
        return True if match else False


def main():
    texts = ["aaaa_bbb", "a_bb", "aabb", "00_00"]
    func = TextValidation.check

    print([func(text) for text in texts])

if __name__ == "__main__":
    main()
