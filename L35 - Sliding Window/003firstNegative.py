from collections import deque

arr = list(map(int, input().split()))
n = len(arr)
k = int(input())

i = 0  # represents start of the window
j = 0  # represents end of the window

# window extends from [i, j)

q = deque()

# 1. find the 1st negative for the 1st window

while j < k:
    if arr[j] < 0:
        q.append(arr[j])
    j += 1


ans = []

if q:
    # 1st window has negative values
    ans.append(q[0])
else:
    # 1st window has no negative values
    ans.append(0)

# 2. find the first negative for the remaining windows

while j < n:
    # slide the window

    if arr[i] < 0:
        q.popleft()
    i += 1
    if arr[j] < 0:
        q.append(arr[j])
    j += 1

    # update the ans
    if q:
        # current window has negative values
        ans.append(q[0])
    else:
        # current window has no negative values
        ans.append(0)

print(ans)

# time : O(n) # space : O(k) due to queue
