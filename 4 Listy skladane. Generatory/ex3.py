examp = (i for i in range(10))
# tworzy obiekt generatora na ktorym stosujemy metode __next__() badz
# globalna funkcje next() lub iterujemy po generatorze za pomoca petli for
print(examp)
print(type(examp)) # <class 'generator'>

for i in range(10):
    if i % 2 == 0:
        print(next(examp))
    else:
        print(examp.__next__())
'''

for iter in examp:
    print(iter)

'''

