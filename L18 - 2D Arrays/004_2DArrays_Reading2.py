m = int(input())
n = int(input())

nums = [[None] * n for _ in range(m)]

for i in range(m):
    nums[i] = list(map(int, input().split()))

for i in range(m):
    for j in range(n):
        print(nums[i][j], end=" ")
    print()
