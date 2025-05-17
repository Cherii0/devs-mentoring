nums = [4, 6, 8, 24, 222, 2]


def func(nums):

    max = nums[0]
    max_idx = 0
    for idx, num in enumerate(nums):
        if num > max:
            max = num
            max_idx = idx


    return max_idx

print(func(nums))


