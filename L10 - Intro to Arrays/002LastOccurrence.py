# time : O(n)


def last_occ(arr: list[int], n: int, t: int) -> int:
    for i in range(n - 1, -1, -1):
        if arr[i] == t:
            return i

    return -1


n = int(input())
t = int(input())

arr = [int(input()) for _ in range(n)]

print(last_occ(arr, n, t))
