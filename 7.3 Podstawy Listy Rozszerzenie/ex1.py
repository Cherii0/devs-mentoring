import re

text = "dowolne zdanie, które bedzie mozna odczytac od konca!"
characters = [
    ",",
    ".",
    ":",
    ";",
    "!",
    "?"
]

for c in characters:
    text = text.replace(c, "")

text = text.split(" ")
text_rev = list(reversed(text)) # new list
text.reverse() # in place

print(text_rev)
print(text)
