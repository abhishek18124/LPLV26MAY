# time : O(n)
# space: O(n) due x[]


def maximum_subarray_sum_using_kadanes(arr: list[int], n: int) -> int:
    x = [None] * n
    x[0] = arr[0]
    max_so_far = x[0]

    for i in range(1, n):
        x[i] = max(x[i - 1] + arr[i], arr[i])
        max_so_far = max(max_so_far, x[i])

    return max_so_far


# time : O(n)
# space: O(1)


def maximum_subarray_sum_using_kadanes_optimised(arr: list[int], n: int) -> int:
    x = arr[0]
    max_so_far = x

    for i in range(1, n):
        x = max(x + arr[i], arr[i])
        max_so_far = max(max_so_far, x)

    return max_so_far


n = int(input())
arr = list(map(int, input().split()))
print(maximum_subarray_sum_using_kadanes(arr, n))
print(maximum_subarray_sum_using_kadanes_optimised(arr, n))
