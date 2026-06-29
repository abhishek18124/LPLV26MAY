# time : O(n^2)


def target_sum_pair(arr: list[int], n: int, t: int) -> int:
    cnt = 0

    for i in range(n - 1):
        for j in range(i + 1, n):
            pair_sum = arr[i] + arr[j]
            if pair_sum == t:
                cnt += 1

    return cnt


# time : O(n)


def target_sum_pair_optimised(arr: list[int], n: int, t: int) -> int:
    cnt = 0
    i, j = 0, n - 1
    while i < j:
        pair_sum = arr[i] + arr[j]
        if pair_sum == t:
            cnt += 1
            i += 1
            j -= 1
        elif pair_sum > t:
            j -= 1
        else:
            # pair_sum < t
            i += 1

    return cnt


n, t = map(int, input().split())
arr = list(map(int, input().split()))
print(target_sum_pair(arr, n, t))
print(target_sum_pair_optimised(arr, n, t))
