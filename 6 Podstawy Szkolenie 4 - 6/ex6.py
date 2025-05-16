a = [3, 1, 5, 7, 9, 2, 6]


print("a ",  a[3])
print("b, ", a[1:4] )
print("c", a[3:] )
print("d ", a[-3:] )
print("e", a[:3] )
print("f ", a[3:-1] )
print("g ", a[::2] )
print("h ", a[5:2:-1] )
print("i " , sum(a) )
print("j ", 8 in a )
print("k ", 4 not in a)

'''

a) a[3] indeksowanie, 4 element z listy
b) a[1:4] indeksowanie, wycinek 2 do 4 elementu włącznie
c) a[3:] indekowanie, każdy element po 4 elemencie włącznie
d) a[-3:] indeksowanie od poczatkowego indeksu -3 tzn od końca 3 elementu, tzn -3 to ostatnie 3 elementu,
-2 to ostatnie 2 elementy pod warunkiem że polecenie to wycinek [-n : ]
e) a[:3] indeksowanie każdy element poza 4 ostatnimi elementami
f) a[3:-1] indekowanie każdy element od 4 elementu włącznie do przedostatniego włącznie
g) a[::2] indeksowanie co drugiego elementu zaczynajac od indeksu 0
h) a[5:2:-1] indeksowanie start:stop:step oznacza że wybierajac wycinek listy od indeksu 5 włącznie do
indeksu 2 nie uwzgledniajac go, zwracamy elementy od końca tego wycinka
i) sum(a) funkcja wbudowania działająca na argumencie listy, sumuje jej elementy
j) 8 in a operator in sprawdzajacy czy wartosc jest obecna w kolekcji zwracajacy wartosc bool
k) 4 not in a negacja operatora in, sprawdza czy wartosc nie jest obecna w kolekcji



'''
