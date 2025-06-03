import re


class TextValidation:

    def __init__(self):
        pass

    @staticmethod
    def contains_only_latin_and_nums(text : str) -> bool:
        """
        print out information whether given text contains non latin letters
        text can not contain whitespaces
        :param text: str
        :return: None
        """
        if not len(text):
            return True

        if not text.isascii():
            return False

        excl_chars = re.findall(pattern=r"[^a-z0-9]", string=text, flags=re.I)
            # second approach
        # excl_chars = re.findall(pattern=r"[^a-zA-Z0-9]", string=text, flags=0)
        excl_chars_len = len(excl_chars)
        return True if excl_chars_len else False


def main():
    texts = ["Gi\nvećn _teg2xt", "04102", "avb", "2a", "90z\nd", "\n","_ 9g",
             "text ", "te_xt"]

    func = TextValidation.contains_only_latin_and_nums
    print([func(text) for text in texts])

if __name__ == "__main__":
    main()
