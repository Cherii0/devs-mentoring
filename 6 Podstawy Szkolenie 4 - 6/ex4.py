while True:
    n = int(input("provide number between 1 and 7..."))

    match n:
        case 1:
            print("poniedzialek")
        case 2:
            print("wtorek")
        case 3:
            print("sroda")
        case 4:
            print("czwartek")
        case 5:
            print("piatek")
        case 6:
            print("sobota")
        case 7:
            print("niedziela")
        case _ :
            print("nie ma takiego dnia")
