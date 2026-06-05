n = int(input())

max_so_far = float("-inf")

for i in range(n):
    x = int(input())
    if x > max_so_far:
        max_so_far = x

print(max_so_far)
