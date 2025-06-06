
import re


class TextValidation:

    def __init__(self):
        pass

    @staticmethod
    def check(text):

        match = re.match(pattern ="^[b0]", string = text, flags=0)
        return True if match else False


def main():
    texts = ["Gi\nvećn", "0_teg2xt", "04102", "avb", "2a", "90z\nd", "\n","_ 9g",
             "text ", "te_xt"]

    func = TextValidation.check
    print([func(text) for text in texts])

if __name__ == "__main__":
    main()
