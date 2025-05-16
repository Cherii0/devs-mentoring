import re

text = 'Napisz program, który wczytuje dowolne zdanie.'
characters = [",", "." ,":" ,";" ,",", "!", "?"]


for c in characters:
    text = text.replace(c, "")

text_words = text.split(" ")

print(text)
print("liczba wyrazow w zdaniu : ", len(text_words))

cap_absent = True

for word in text_words:
    if word[0].isupper():
        cap_absent = False
        print(word)


if cap_absent:
    print("nie ma wyrazow na duza litere ")

find_words = [ "i", "w" , "na", "pod", "dla"]
summary = {}
for word in text_words:
    if word in find_words:
        summary[word] = text_words.index(word)

if len(summary) > 0:
    print(summary)
else:
    print("poszukiwanych wyrazow nie ma w tekscie")


text_words.sort()
text_words.reverse()
print(text_words)
