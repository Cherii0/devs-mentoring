albums = {
        'The Sensual World' : 'Kate Bush',
        'Shaday' : 'Ofra Haza',
        'Achtung Baby' : 'U2',
        'Aion' : 'Dead Can Dance',
        'Invisible Touch' : 'Genesis'
}

for album in albums.keys():
    print(album)

usr_album = input("podaj swoj album... ")

if usr_album in albums.keys() :
    print(f"Wykonawca albumu {usr_album} jest {albums[usr_album]}")
else :
    print("Brak danych")
