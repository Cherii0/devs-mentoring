from operator import concat

colors = [('red', 'pink'), ('white', 'black'), ('orange', 'green')]
converted = list(map(lambda pair : pair[0] + " " + pair[1], colors))
converted2 = list(map(lambda pair : concat(pair[0],  pair[1]), colors))

print(converted)
print(converted2)