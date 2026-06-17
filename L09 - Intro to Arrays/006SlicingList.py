nums = [10, 20, 30, 40, 50]

sl = nums[1:4]
print(sl)
print(type(sl))

sl[0] = 11
sl[1] = 21
sl[2] = 31

print(sl)
print(nums)

nums[0] = 100
print(nums)

print(nums[:4])  # [0, 4)

print(nums[3:])  # [3, n)

print(nums[:])  # [0, n) # we can use this code to create a copy of a list

print(nums[1:4:2])  # [1, 4) in steps of 2s

print(nums[::-1])  # we can use this code to create a reversed copy of a list

colors = ["red", "green", "blue", "white"]
print(colors)

colors[1:3] = ["pink", "black"]

print(colors)

colors[0] = "violet"

print(colors)

colors[1:3] = ["orange"]

print(colors)

colors[0:2] = ["yellow", "mustard", "neon"]

print(colors)

arr = [10, 20, 30, 40, 50]
arr[0:3:2] = [100, 300]
print(arr)
