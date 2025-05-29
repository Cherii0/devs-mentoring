import math

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

nums_even = list(filter(lambda num : num % 2 == 0, nums))

nums_pow = list(map(lambda num : math.pow(num,2), nums_even))

print(nums_pow)