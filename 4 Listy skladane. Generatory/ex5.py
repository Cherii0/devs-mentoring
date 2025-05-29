
source_text = "The quick brown fox jumps over the lazy dog is an " \
              "English-language pangram—a sentence that contains all " \
              "of the letters of the English alphabet"

filtered_text = [word for word in source_text.split(" ") if word not in ["The", "the"]]

length_words = [len(word) for word in filtered_text]

print(length_words)