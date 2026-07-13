# time : O(m+n)
def is_present(nums: list[list[int]], m: int, n: int, t: int) -> bool:
    i, j = 0, n - 1
    while i <= m - 1 and j >= 0:
        if nums[i][j] == t:
            return True
        elif t > nums[i][j]:
            i += 1
        else:
            # t < nums[i][j]
            j -= 1

    # t is not present in the nums[][]
    return False


m, n = map(int, input().split())

nums = [[None] * n for _ in range(m)]

for i in range(m):
    nums[i] = list(map(int, input().split()))

t = int(input())

print(is_present(nums, m, n, t))
