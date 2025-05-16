# part 1
width = 7
lenght = 6

line = "*" * width

for i in range(lenght):
    print(line)


# part 2
width = 5
lenght = 5

full_line = "*  " * width
blank_line = "* " + ("  " * width) + "*"

for i in range(lenght):
    if i == 0:
        print(full_line)
    elif i < lenght -1 :
        print(blank_line)
    else:
        print(full_line)

# part 3

lenght = 5

for i in range(0, lenght):
    print(" " * (lenght- i) +  "*" * i + "*" * (i+1))
