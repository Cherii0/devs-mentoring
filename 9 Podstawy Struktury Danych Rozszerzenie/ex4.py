dataset = set()
dataset_res = []

while True:

    data_line = input("podaj pare Miasto opad oddzielone spacjami ")

    # pusta linia - koniec programu.
    if len(data_line) == 0:
        break
    else:
        dataset.add(data_line)



for elem in dataset.copy():
    new_elem = elem.replace(" ", " : ")
    dataset_res.append(new_elem)

print(dataset_res)
