fav_col = {"black",
           "darkblue",
           "yellow"}

usr_col = set(input("podaj swoje ulubione kolory oddzielone spacjami : ").split(" "))

equal_sets = usr_col == fav_col
if equal_sets:
    print("zbiory sa identyczne" )
else:

    print("wspolne kolory :",fav_col.intersection(usr_col))
    print("kolory wybrane tylko przez uzytkownika:",usr_col.difference(fav_col))
    print("kolory wybrane tylko przez programiste:",fav_col.difference(usr_col))
