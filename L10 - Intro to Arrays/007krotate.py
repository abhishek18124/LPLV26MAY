# time : O(kn)


def k_rotate(arr: list[int], n: int, k: int) -> None:
    for _ in range(k):
        for i in range(n - 1, 0, -1):
            arr[i], arr[i - 1] = arr[i - 1], arr[i]


n = int(input())
k = int(input())
arr = [int(input()) for _ in range(n)]

print(arr)
k_rotate(arr, n, k)
print(arr)
