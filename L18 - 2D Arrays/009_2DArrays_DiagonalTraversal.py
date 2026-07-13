# time : In worst case print_diagonal takes O(min(m, n))
def print_diagonal(nums: list[list[int]], m: int, n: int, i: int, j: int) -> None:
    # print the diagonal that starts at the i,jth index
    while i < m and j < n:
        print(nums[i][j], end=" ")
        i += 1
        j += 1
    print()


m, n = map(int, input().split())

nums = [[None] * n for _ in range(m)]

for i in range(m):
    nums[i] = list(map(int, input().split()))

for i in range(m):
    print_diagonal(nums, m, n, i, 0)

for j in range(1, n):
    print_diagonal(nums, m, n, 0, j)

# total time : (m + n - 1) * min(m, n)
