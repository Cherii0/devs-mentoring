from functools import reduce
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
nums3 = [7, 8, 9]

print(reduce(lambda total, num : total + num, nums1))
print(reduce(lambda total, num : total + num, nums2))
print(reduce(lambda total, num : total + num, nums3))