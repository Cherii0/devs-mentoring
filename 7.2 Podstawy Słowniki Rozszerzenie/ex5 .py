import math

n = int(input("podaj granice ciagu"))

nums_squares = {}

for i in range(1, n+1):
    nums_squares[i] = int(math.pow(i, 2))


print(nums_squares)
