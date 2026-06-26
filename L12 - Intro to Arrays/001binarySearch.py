# time : O(logn)
def binary_search(arr: list[int], n: int, t: int) -> int:
    lo, hi = 0, n - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == t:
            # t is found at idx mid
            return mid
        elif t > arr[mid]:
            lo = mid + 1
        else:
            # t < arr[mid]
            hi = mid - 1

    # t is not present in arr[]
    return -1


n, t = map(int, input().split())
arr = list(map(int, input().split()))

print(binary_search(arr, n, t))
