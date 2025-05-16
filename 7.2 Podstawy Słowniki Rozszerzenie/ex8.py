from itertools import count

dict = { "V":"S001", "VI": "S002", "VII": "S001", "VIII": "S005", "IX":"S005", "X":"S009", "XI":"S007" }
all_values = []

for value in dict.values():
    all_values.append(value)

for value in all_values:
    occurence = all_values.count(value)
    if occurence == 1:
        print(value)
