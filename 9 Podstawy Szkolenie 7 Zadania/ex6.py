def func(nums):

    res = filter(lambda x : x<= -10 or x >= 10, nums)
    return list(res)


print(func([i for i in range(5,15)]))
print(func([i for i in range(-15,-5)]))
