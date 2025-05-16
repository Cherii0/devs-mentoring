albums = {
        'The Sensual World' : 'Kate Bush',
        'Shaday' : 'Ofra Haza',
        'Achtung Baby' : 'U2',
        'Aion' : 'Dead Can Dance',
        'Invisible Touch' : 'Genesis'
}    

while True:
    print("1 - dodaj album")
    print("2 - usun album")
    print("3 - sprawdz album i wykonawce")
    print("4 - sprawdz albumy")
    n = int(input("co chcesz zrobic ? "))

    match n:
        case 1:
            usr_album = input("podaj album do dodania ... ")
            usr_auth = input("podaj autora albumu ... ")
            albums[usr_album] = usr_auth
        case 2:
            usr_album = input("podaj album do usuniecia ... ")
            if usr_album in albums.keys():
                del albums[usr_album]
                print("album usuniety")
            else:
                print("Brak podanego albumu w słowniku ")
        case 3:
            usr_album = input("podaj swoj album... ")
            if usr_album in albums.keys():
                print(f"Wykonawca albumu {usr_album} jest {albums[usr_album]}")
            else:
                print("Brak danych")
        case 4:
            for album in albums.keys():
                print(album)



