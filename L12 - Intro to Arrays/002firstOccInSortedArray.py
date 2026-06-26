# time : O(logn)
def first_occ(arr: list[int], n: int, t: int) -> int:
    lo, hi = 0, n - 1
    ans = -1

    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == t:
            # t is found at idx mid
            ans = mid
            hi = mid - 1
        elif t > arr[mid]:
            lo = mid + 1
        else:
            # t < arr[mid]
            hi = mid - 1

    return ans


n, t = map(int, input().split())
arr = list(map(int, input().split()))

print(first_occ(arr, n, t))
