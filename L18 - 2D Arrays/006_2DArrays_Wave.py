def wave_print(nums: list[list[int]], m: int, n: int) -> None:
    for j in range(n):
        if j % 2 == 0:
            # jth column is even
            for i in range(m):
                print(nums[i][j], end=" ")
        else:
            # jth column is odd
            for i in range(m - 1, -1, -1):
                print(nums[i][j], end=" ")


m, n = map(int, input().split())

nums = [[None] * n for _ in range(m)]

for i in range(m):
    nums[i] = list(map(int, input().split()))

wave_print(nums, m, n)
