# z bledami
plik = open("przyklad.txt", "r")
linie = plik.readlines()
print(linie)

# poprawne

plik = open("przyklad.txt", "r", encoding="utf-8")
linie = plik.readlines()
print(linie)
plik.close()

'''

brak zalaczenia odpowiednij tablicy dekodujacej : encoding = "utf-8"
brak zamkniecia pliku : plik.close()

'''
