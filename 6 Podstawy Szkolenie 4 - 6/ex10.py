from random import randint

while True:

    bottom_range = int(input("podaj dolna granice : "))
    upper_range = int(input("podaj gorna granice : "))

    points = upper_range - bottom_range

    quessed_num = randint(bottom_range, upper_range)

    while True:
        quess = int(input("podaj liczbe ktora wylosował program... "))

        if quessed_num == quess:
            print(f"Gratulacje zdobyłes {points} punktow!")
            break
        elif quess < quessed_num:
            points -= 1
            print("za mało")
        else:
            points -= 1
            print("za duzo")

    print("---------------   nowa gra ---------------------")
