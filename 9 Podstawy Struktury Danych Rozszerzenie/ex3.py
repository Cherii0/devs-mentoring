original_dict = {"a" : 3, "b" : 1, "c" : 10, "d" : 15, "e" : 20}
keys = list(original_dict.keys())
values = list(original_dict.values())
reverse_dict = dict()

for key, value in zip(keys, values):
    reverse_dict[value] = key


print(original_dict)
print(reverse_dict)
