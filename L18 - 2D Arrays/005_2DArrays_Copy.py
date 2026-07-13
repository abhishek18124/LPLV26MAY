import copy

nums = [[10, 20], [30, 40], [50, 60]]
# nums_copy = nums[:]
nums_copy = copy.deepcopy(nums)
print(nums)
print(nums_copy)
print()

nums_copy[0][0] = 100

print(nums)
print(nums_copy)

# a = [10, 20, 30]
# b = a[:]
# b[0] = 100
# print(a)
# print(b)
