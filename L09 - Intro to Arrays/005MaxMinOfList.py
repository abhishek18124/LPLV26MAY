nums = [10, 20, 30, 40, 50]

max_so_far = float("-inf")  # -math.inf
for num in nums:
    if num > max_so_far:
        max_so_far = num

print(max_so_far)

print(max(nums))

min_so_far = float("inf")
for num in nums:
    if num < min_so_far:
        min_so_far = num

print(min_so_far)

print(min(nums))
