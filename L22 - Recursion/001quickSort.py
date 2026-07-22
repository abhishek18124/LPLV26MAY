def partition(arr: list[int], lo: int, hi: int) -> None:
    i = lo
    pivot = arr[hi]

    for j in range(lo, hi):  # [lo, hi)
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
        j += 1

    arr[i], arr[hi] = arr[hi], arr[i]
    return i


def f(arr: list[int], lo: int, hi: int) -> None:
    # base case

    # if lo == hi:  # optional
    #     return

    # if lo > hi:  # mandatory
    #     return

    if lo >= hi:
        return

    # recursive case

    # 1. partition the arr[lo..hi] around the pivot i.e. arr[hi]
    pi = partition(arr, lo, hi)

    # 2. ask your friend to sort arr[lo...pi-1]
    f(arr, lo, pi - 1)

    # 3. ask your friend to sort arr[pi+1...hi]
    f(arr, pi + 1, hi)


arr = list(map(int, input().split()))
n = len(arr)

f(arr, 0, n - 1)

# print(arr)
print(*arr)
