# # time : O(n^3)
# def maximum_subarray_sum(arr: list[int], n: int) -> int:
#     max_so_far = float("-inf")
#     for i in range(n):
#         for j in range(i, n):
#             # find the sum of the subarray
#             # that starts at the ith index
#             # and ends at the jth index
#             max_so_far = max(max_so_far, sum(arr[i : j + 1]))

#     return max_so_far


# time : O(n^3)
def maximum_subarray_sum(arr: list[int], n: int) -> int:
    max_so_far = float("-inf")
    for i in range(n):
        for j in range(i, n):
            # find the sum of the subarray
            # that starts at the ith index
            # and ends at the jth index
            s = 0  # to track the sum of arr[i..j]
            for k in range(i, j + 1):
                s += arr[k]
            max_so_far = max(max_so_far, s)

    return max_so_far


n = int(input())
arr = list(map(int, input().split()))
print(maximum_subarray_sum(arr, n))
