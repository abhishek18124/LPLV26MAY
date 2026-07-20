def merge(arr: list[int], lo: int, mid: int, hi: int) -> None:
    temp = []

    i = lo  # to iterate over arr[lo...mid]
    j = mid + 1  # to iterate over arr[mid+1...hi]

    while i <= mid and j <= hi:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1

    while i <= mid:
        temp.append(arr[i])
        i += 1

    while j <= hi:
        temp.append(arr[j])
        j += 1

    arr[lo : hi + 1] = temp


def f(arr: list[int], lo: int, hi: int) -> None:
    # base case
    if lo == hi:
        # f(lo, hi) : sort the arr[lo...lo] or arr[hi...hi]
        return

    # recursive case

    # f(lo, hi) : sort the arr[lo...hi] using merge sort

    # 1. divide the arr[lo...hi] around the mid point
    mid = (lo + hi) // 2

    # 2.1 ask your friend to sort the left half i.e. arr[lo...mid]
    f(arr, lo, mid)

    # 2.2 ask your friend to sort the right half i.e. arr[mid+1...hi]
    f(arr, mid + 1, hi)

    # 3. merge the two sorted halves arr[lo...mid] and arr[mid+1...hi]
    merge(arr, lo, mid, hi)


arr = [60, 50, 40, 30, 20, 10]
f(arr, 0, len(arr) - 1)
print(arr)
