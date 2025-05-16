import re

birds = {
        'kos' : 'Turdus merula',
         'wilga' : 'Oriolus oriolus',
         'rudzik' : 'Erithacus rubecula',
         'kukulka' : 'Cuculus canorus',
         'pleszka' : 'Phoenicurus phoenicurus',
         'bogatka' : 'Parus major',
         'drozd' : 'Turdus philomelos',
         'zieba' : 'Fringilla coelebs',
         'dzwoniec' : 'Chloris chloris',
         'szczygiel' : 'Carduelis carduelis',
         'szpak' : 'Sturnus vulgaris',
         'kopciuszek' : 'Phoenicurus ochruros'
}

text = "W polowie maja, juz przed wschodem slonca, o trzeciej zaczyna spiewac drozd, po nim rudzik, a chwile pozniej kos. Pol godziny pozniej odzywa sie kukulka. Zaraz po niej budzi sie bogatka. Wraz ze wschodem slonca, o czwartej godzinie, swoj koncert rozpoczynaja pleszka i zieba. Dwadziescia minut pozniej i wilga akcentuje swoja obecnosc wysoko w koronach drzew. Jeszcze pozniej swoje trzy grosze dodaje szpak, a tuz po nim kopciuszek. Najwiekszymi spiochami w tej ferajnie okazuja sie byc dzwoniec i szczygiel."

words_text = re.split(" |, |\.",  text )
print(words_text)

for word in words_text:
    if word in birds.keys():
        lat_name = "(" + birds[word] +  ")"
        text = text.replace(word, (word + lat_name))

print(text)
