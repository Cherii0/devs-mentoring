list_len = 3
destination_list = []

while list_len > 0:
    inputed_num = int(input("provide number... "))
    destination_list.append(inputed_num)
    list_len = list_len - 1

print(list(filter(lambda x : x % 2 == 0, destination_list)))
