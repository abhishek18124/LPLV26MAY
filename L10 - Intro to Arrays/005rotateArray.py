# time : O(n)


def rotate(arr: list[int], n: int) -> None:
    temp = arr[-1]

    for i in range(n - 1, 0, -1):
        arr[i] = arr[i - 1]

    arr[0] = temp


n = int(input())
arr = [int(input()) for _ in range(n)]

print(arr)
rotate(arr, n)
print(arr)
