import random

result = [12,1,45,76,50,23]

for elem in result:
    if elem > 49 or elem < 1:
        result[result.index(elem)] = random.randint(1,49)

print(result)

# -----

import random
from random import randint

wynik = [12,1,45,76,50,23]

for elem in wynik:
    if elem > 49 or elem < 1:
        wynik[wynik.index(elem)] = random.randint(1,49)

print(wynik)
