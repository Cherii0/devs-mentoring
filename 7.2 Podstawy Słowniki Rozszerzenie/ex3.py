text = "Once upon a midnight dreary, while I pondered, weak and weary, Over many a quaint and curious volume of forgotten lore, While I nodded, nearly napping, suddenly there came a tapping, As of someone gently rapping, rapping at my chamber door. This visitor, I muttered, tapping at my chamber door - Only this, and nothing more."


list_words = text.split(" ")

unique_words = set(list_words)

word_occurence = {}

for word in unique_words:
    word_occurence[word] = list_words.count(word)

print(word_occurence)
