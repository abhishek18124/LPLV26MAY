nums = [20, 30, 40, 50, 60]
print(nums)

nums.insert(0, 10)
print(nums)

nums.insert(2, 25)
print(nums)

print(nums.pop(0))
print(nums)

print(nums.pop(2))
print(nums)

nums.append(70)  # const time
print(nums)

print(nums.pop())  # const time
print(nums)

nums_1 = [10, 20, 30]
nums_2 = [40, 50, 60]

nums_1.extend(nums_2)

# nums_1 = nums_1 + nums_2

print(nums_1)
