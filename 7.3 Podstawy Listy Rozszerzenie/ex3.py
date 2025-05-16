lista1 = ["abc", "def", "ghi", "jkl"]
lista2 = [1, 2, 3, 4, 5]
lista3 = ["xyz", 1, '2'] 


# wydrukowanie list

print(lista1)
print(lista2)
print(lista3)

# wydrukowanie 1 oraz 4 elementu z lity 1

if len(lista1) > 3:
    print("elementy 1 oraz 4 : ", lista1[0], lista1[3])

# przypisanie drugiemu elementowi z listy2

lista2[1] = lista3[1]
print(lista2)

# przypisanie trzeciemu elementowi listy 3 wartosc z klawiatury

lista3[2] = input("podaj wartosc ... ")
print(lista3)

# doda nowy element slowo do listy1
lista1.append("slowo")
print(lista1)


# kasowanie elementu na pozycji/indeksie 2 z lista1


lista1.remove(lista1[2])
print(lista1)


# liczba elementow w liscie 3

print(len(lista3))

# powiekszy liste 1 o elementy listy 3

lista1.extend(lista3)

print(lista1)
