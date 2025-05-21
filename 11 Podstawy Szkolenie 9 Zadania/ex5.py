
class Desk:

    def __init__(self):

        self.__figures = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.__values = [str(n) for n in range(2,11)] + ["Jack", "Queen", "King", "Ace"]
        self.__cards = []

        for figure in self.__figures:
            for value in self.__values:
                self.__cards.append(Card(figure, value))


    def deal(self):
        return self.__cards.pop()

    def shuffle(self):
        import random
        random.shuffle(self.__cards)

    def describe_cards(self):
        for card in self.__cards:
            print(card)

class Card:

    def __init__(self, figure, value):

        self.__figure = figure
        self.__value= value

    def __str__(self):
        return f"{self.__figure} {self.__value}"


def main():
    desk = Desk()
    
    # before deal()
    desk.shuffle()
    desk.describe_cards()
    # print() force Card object to use __str__ magic method
    print(f"given card : { desk.deal()}")
    # after deal()
    desk.describe_cards()



if __name__ == '__main__':
    main()
