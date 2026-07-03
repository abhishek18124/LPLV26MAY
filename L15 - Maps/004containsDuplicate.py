from collections import defaultdict

# time : O(n)
# space: O(n) due freq_map


def is_duplicate_present(arr: list[int], n: int) -> bool:
    # freq_map = dict()  # {}
    # for x in arr:
    #     # if x in freq_map:
    #     #     freq_map[x] = freq_map[x] + 1
    #     # else:
    #     #     freq_map[x] = 1
    #     freq_map[x] = freq_map.get(x, 0) + 1

    freq_map = defaultdict(int)
    for x in arr:
        freq_map[x] = freq_map[x] + 1
        if freq_map[x] > 1:
            return True

    return False

    # for x, freq in freq_map.items():
    #     print(x, freq)


n = int(input())
arr = list(map(int, input().split()))
print(is_duplicate_present(arr, n))
