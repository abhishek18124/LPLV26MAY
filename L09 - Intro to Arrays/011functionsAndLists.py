def compute_sum(nums: list[int]) -> int:
    s = 0
    for num in nums:
        s += num
    return s


def modify_nums(nums: list[int]) -> int:
    for i in range(len(nums)):
        nums[i] += 1


nums = [10, 20, 30, 40, 50]
print(compute_sum(nums))

print(nums)

modify_nums(nums)

print(nums)
