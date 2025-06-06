
import re


class TextValidation:

    def __init__(self):
        pass

    @staticmethod
    def check(text):
        
        words = re.split(pattern = " ", string=text)
        p = r"[s]{2}$"
        found_words = list(filter(lambda word : re.search(pattern = p, string = word), words))
        return found_words



def main():
    texts = ["przykladowy tekss w programie pythonss"]
    func = TextValidation.check

    print(*[func(text) for text in texts])

if __name__ == "__main__":
    main()
