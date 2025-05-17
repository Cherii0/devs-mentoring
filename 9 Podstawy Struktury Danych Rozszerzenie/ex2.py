from random import randint

numbers  = set()
numbers_len = 4
bottom_border = 5
upper_border = 120

while len(numbers) != numbers_len:
    n = randint(bottom_border, upper_border)
    if n not in numbers:
        numbers.add(n)


numbers_odd = list(filter(lambda n : n % 2 != 0, numbers))

print(numbers)
print(numbers_odd)





