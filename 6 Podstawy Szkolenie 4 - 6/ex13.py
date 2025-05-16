def start_menu():
    print("1 - dodawanie słowa z definicja")
    print("2 - znajdz definicje slowa")
    print("3 - usun slowo oraz definicje")
    print("4 - koniec programu")


words_dict = {}

while True:

    start_menu()
    choice = int(input("twoj wybor : "))

    match choice:
        case 1:
            word = input("podaj slowo :")
            word_expl = input("podaj definicje slowa :")
            words_dict[word] = word_expl
        case 2:
            word = input("podaj szukane slowo : ")
            if word in words_dict.keys():
                print(f"definicja slowa {word} : ", words_dict[word])
            else:
                word = input(f"nie ma takiego slowa jak {word}, podaj szukane slowo : ")
        case 3:
            word = input("podaj slowo ktore ma zostac usuniete : ")
            if word in words_dict.keys():
                del words_dict[word]
            else:
                word = input(f"nie ma takiego slowa jak {word}, podaj slowo ktore ma zostac usuniete : ")

        case 4:
            break


