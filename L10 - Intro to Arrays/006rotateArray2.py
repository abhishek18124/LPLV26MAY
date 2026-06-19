# time : O(n)


def rotate(arr: list[int], n: int) -> None:
    for i in range(n - 1, 0, -1):
        arr[i], arr[i - 1] = arr[i - 1], arr[i]


n = int(input())
arr = [int(input()) for _ in range(n)]

print(arr)
rotate(arr, n)
print(arr)
