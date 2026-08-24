arr = list(map(int, input().split()))
n = len(arr)
k = int(input())

i = 0  # represents start of the window
j = 0  # represents end of the window

# window extends from [i, j)

w_sum = 0

# 1. find the sum of the 1st window

while j < k:
    w_sum += arr[j]
    j += 1

max_so_far = w_sum

# 2. find the sum for the remaining windows

while j < n:
    # slide the window

    w_sum -= arr[i]
    i += 1
    w_sum += arr[j]
    j += 1

    max_so_far = max(max_so_far, w_sum)

print(max_so_far)

# time : O(n) # space : O(1)
