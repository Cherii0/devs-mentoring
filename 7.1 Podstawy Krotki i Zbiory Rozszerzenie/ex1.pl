colors = [
    'zielony', 'czerwony', 'niebieski', 'czarny',
    'fioletowy', 'granatowy', 'niebieski', 'czarny',
    'czarny', 'zielony', 'cytrynowy', 'granatowy',
    'niebieski', 'indygo', 'zielony','czerwony'
]

unique_colors = set(colors)

print("oryginalna lista zawiera ",  len(colors), "kolorow")
print("ilosc uzytych kolorow : ", len(unique_colors))

for color in unique_colors:
    print(color)

unique_colors.add("rozowy")

print(unique_colors) # za kazdym razem inne miejsce w kolekcji - nieuporzadkowane

unique_colors.remove("granatowy") # elementy pozostaja na swoich miejscach

print(unique_colors)
