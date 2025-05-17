bill_items = [
    ['Tom', 'Calamari', 6.00],
    ['Tom', 'American Hot', 11.50],
    ['Tom', 'Chocolate Fudge Cake', 4.45],
    ['Clare', 'Bruschetta Originale', 5.35],
    ['Clare', 'Fiorentina', 10.65],
    ['Clare', 'Tiramisu', 4.90],
    ['Rich', 'Bruschetta Originale', 5.35],
    ['Rich', 'La Reine', 10.65],
    ['Rich', 'Honeycomb Cream Slice', 4.90],
    ['Rosie', 'Garlic Bread', 4.35],
    ['Rosie', 'Veneziana', 9.40],
    ['Rosie', 'Tiramisu', 4.90],
]

result_dict = {}
food = []
price = 0
name = ""
name_temp = bill_items[0][0]



for item in bill_items:
    name = item[0]
    if name != name_temp:
        result_dict[name_temp] = {"potrawy" : food, "cena" : price}
        food.clear()
        price = 0
    else:
        food.append(item[1])
        price += item[-1]

    name_temp = name


print(result_dict)



