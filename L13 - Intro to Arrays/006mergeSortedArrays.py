# time : O(n+m)
def merge_sorted_arrays(a: list[int], b: list[int], n: int, m: int) -> None:
    i, j, k = 0, 0, 0
    c = [None] * (n + m)

    while i <= n - 1 and j <= m - 1:
        if a[i] <= b[j]:
            c[k] = a[i]
            i += 1
            k += 1
        else:
            c[k] = b[j]
            j += 1
            k += 1

    while i <= n - 1:
        c[k] = a[i]
        i += 1
        k += 1

    while j <= m - 1:
        c[k] = b[j]
        j += 1
        k += 1

    print(c)


a = [10, 30, 50, 60]
n = len(a)

b = [20, 40, 70]
m = len(b)

merge_sorted_arrays(a, b, n, m)
