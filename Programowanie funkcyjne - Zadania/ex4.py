
lines = ["10000101011", "111111", "01010101010010", "011001100001", "001010101011"]
print(sum(list(map(lambda elem : 0 if elem.count("11") == 0 else 1,  lines))))
