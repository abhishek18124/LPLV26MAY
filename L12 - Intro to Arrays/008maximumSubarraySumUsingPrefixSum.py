# time : n + n^2 ~ O(n^2)
# space : O(n) due to pSum[]
def maximum_subarray_sum(arr: list[int], n: int) -> int:
    pSum = [None] * n

    pSum[0] = arr[0]
    for i in range(1, n):
        pSum[i] = pSum[i - 1] + arr[i]

    max_so_far = float("-inf")
    for i in range(n):
        for j in range(i, n):
            # find the sum of the subarray
            # that starts at the ith index
            # and ends at the jth index
            s = pSum[j] if i == 0 else pSum[j] - pSum[i - 1]
            max_so_far = max(max_so_far, s)

    return max_so_far


n = int(input())
arr = list(map(int, input().split()))
print(maximum_subarray_sum(arr, n))
