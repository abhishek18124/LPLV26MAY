# time : n^2.const ~ O(n^2)
def transpose(nums: list[list[int]], n: int) -> None:
    for i in range(n):
        for j in range(n):
            if i < j:
                nums[i][j], nums[j][i] = nums[j][i], nums[i][j]


# time : (n^2-n)/2 . const ~ O(n^2)
def transpose_optmised(nums: list[list[int]], n: int) -> None:
    for i in range(n):
        for j in range(i + 1, n):
            nums[i][j], nums[j][i] = nums[j][i], nums[i][j]


n = int(input())

nums = [[None] * n for _ in range(n)]

for i in range(n):
    nums[i] = list(map(int, input().split()))

# transpose(nums, n)
transpose_optmised(nums, n)

for i in range(n):
    for j in range(n):
        print(nums[i][j], end=" ")
    print()
