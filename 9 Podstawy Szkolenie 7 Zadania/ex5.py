def func(**kwargs):

    res = []
    odd = []
    even = []
    for key, value in kwargs.items():
        if value % 2 == 1:
            odd.append(value)
        else:
            even.append(value)

    len_odd = len(odd)
    len_even = len(even)
    nums_len = len_even

    if len_even > len_odd:
        nums_len = len_odd

    for i in range(nums_len):
        res.append(odd[i])
        res.append(even[i])

    if len_even == len_odd:
        return res

    if nums_len == len_even:
        res.extend(odd[nums_len:])
    else:
        res.extend(even[nums_len:])

    return res


print(func(a = 1, b = 3, c = 6, d = 8, e = 12))
