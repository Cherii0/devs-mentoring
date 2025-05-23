
class Menu:

    def show(self):
        print("1. Dodaj notatkę")
        print("2. Dodaj wizytówkę (Card)")
        print("3. Wyświetl wszystkie notatki")
        print("4. Wyświetl wszystkie wizytówki")
        print("5. Wyjdź")

    def get_choice(self):
        return input("Podaj wybor : ")

class NotesSubManager:

    def __init__(self):
        self.__notes = []

    def add(self):
        note = input("Podaj notatke : ")
        if note not in self.__notes:
            self.__notes.append(note)

    def show(self):

        if not self.__notes:
            print("Nie masz zadnych notatek")
            return

        print("Twoje notatki :")
        for no, note in enumerate(self.__notes, start=1):
            print(f"{no}. : {note}")


class CardsSubManager:

    def __init__(self):
        self.__cards = []

    def add(self):
        card = input("Podaj notatke : ")
        if card not in self.__cards:
            self.__cards.append(card)

    def show(self):

        if not self.__cards:
            print("Nie masz zadnych wizytowek")
            return

        print("Twoje wizytowki :")
        for no, card in enumerate(self.__cards, start=1):
            print(f"{no}. : {card}")



class Manager(Menu, CardsSubManager, NotesSubManager):

    def __init__(self):
        Menu.__init__(self)
        CardsSubManager.__init__(self)
        NotesSubManager.__init__(self)

    def start(self):
        self.show()

    def show_menu(self):
        self.show()

    def show_notes(self):
        NotesSubManager.show(self)

    def show_cards(self):
        CardsSubManager.show(self)

    def execute(self):

        choice = self.get_choice()
        while choice != "5":
            match choice:
                case "1":
                    NotesSubManager.add(self)
                case "2":
                    CardsSubManager.add(self)
                case "3":
                    self.show_notes()
                case "4":
                    self.show_cards()
                case "5":
                    break
                case _ :
                    print("Podaj wybor z zakresu 1-5 ")
            choice = self.get_choice()


def main():

    manager = Manager()
    manager.start()
    manager.execute()

if __name__ == "__main__":
    main()
