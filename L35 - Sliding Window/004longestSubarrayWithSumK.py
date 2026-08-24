arr = list(map(int, input().split()))
n = len(arr)
k = int(input())

i = 0  # represents start of the window
j = 0  # represents end of the window

# window extends from [i, j)

w_sum = 0
max_so_far = 0

while j < n:
    # expand the window

    w_sum += arr[j]
    j += 1

    # if w_sum > k:
    # 	# current window is invalid so start shrinking the window
    #     while w_sum > k:
    #         w_sum -= arr[i]
    #         i += 1

    while w_sum > k:
        # current window is invalid so start shrinking the window
        w_sum -= arr[i]
        i += 1

    if w_sum == k:
        # current window is valid
        max_so_far = max(max_so_far, j - i)

print(max_so_far)

# time : n + n ~ O(n)
# space: O(1)
