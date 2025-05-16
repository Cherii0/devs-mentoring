import random
from random import randint

wynik = [12,1,45,76,50,23]

for elem in wynik:
    if elem > 49 or elem < 1:
        wynik[wynik.index(elem)] = random.randint(1,49)

print(wynik)
