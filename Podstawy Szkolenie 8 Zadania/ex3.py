lines_raw = []
lines_even = []

with open("przyklad_zad_3.txt", "r", encoding="utf-8") as file:
    lines_raw.extend(file.readlines())


for n, line in enumerate(lines_raw, start=1 ):
    if n % 2 == 0:
        lines_even.append(line)

print(lines_even)
