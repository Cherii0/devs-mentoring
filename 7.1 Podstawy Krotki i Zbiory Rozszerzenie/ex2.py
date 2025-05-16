while True:

    sample_sentence = input("podaj swoje zdanie : ")

    exclude_elements = [",", ".", ":", ";", "!", "?"]

    corrected_sentence = "".join([letter for letter in sample_sentence if letter not in exclude_elements])

    print("po usunieciu znakow : ", corrected_sentence)

    # tuple pozwalaja na duplikaty

    total_words = 0
    words = tuple(corrected_sentence.split(" "))
    for word in set(words):
        n = words.count(word)
        print(word, " : ", n)
        total_words += n
    print("wszystkich slow : ", total_words)

    res_line = ""
    for word in words:
        res_line += "".join(word)

    print(res_line)

    if len(words) >= 4:
        print("wyraz 1 : ", words[0], "wyraz 4 : ", words[3])
    else:
        print("za malo wyrazow")

    # zbiory nie pozwalaja na duplikaty
    # korzystajac z metod zbiorow

    set_corrected_sentence = set(corrected_sentence.split(" "))
    unique_words = len(set_corrected_sentence)
    print("unikalnych slow : ", unique_words)

    res_line = ""
    for word in set_corrected_sentence:
        res_line += "".join(word)

    print(res_line)
    list_set =  list(set_corrected_sentence)

    if len(set_corrected_sentence) >= 4:
        first_elem = list_set[0]
        fourth_elem = list_set[3]
        print("wyraz 1 : ",first_elem, "wyraz 4 : ",fourth_elem )
    else:
        print("za malo wyrazow")


    if fourth_elem == first_elem:
        print(f"elementy {first_elem} oraz {fourth_elem} sa takie same")
    else:
        print(f"elementy {first_elem} oraz {fourth_elem} sa rozne")

