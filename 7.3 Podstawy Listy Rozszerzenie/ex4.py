names = input("podaj imiona znajomych oddzielone spacjami : ")

for name in names.split(" "):

    match name:
        case "Adrian":
            print("Hej Adrian")
        case "Piotrek":
            print("Czesc Piotrek")
        case "Paweł":
            print("Siema Pawel")
        case "Kuba":
            print("Witaj Kuba")
        case _:
            print("Witaj nieznajomy")
