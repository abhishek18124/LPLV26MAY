n = int(input())
arr = list(map(int, input().split()))

# time : O(n)
# space: O(1) but we've modifed the arr[]

for x in arr:
    x = x % n
    arr[x] += n

for i, x in enumerate(arr):
    if (x // n) > 1:
        print(i)
