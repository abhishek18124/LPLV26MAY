m = int(input())
n = int(input())

nums = [[0] * n for _ in range(m)]
print(nums)

for i in range(m):
    for j in range(n):
        print(nums[i][j], end=" ")
    print()
