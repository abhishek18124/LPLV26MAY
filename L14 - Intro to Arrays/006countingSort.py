n, k = map(int, input().split())
arr = list(map(int, input().split()))

freq = [0] * (k + 1)
# time : O(n)
for x in arr:
    freq[x] += 1

# print(freq)

# for i, x in enumerate(freq):
#     print("freq[", i, "] = ", x)

# time : O(n + k)
for i in range(k + 1):
    # print 'i' freq[i] times
    for _ in range(freq[i]):
        print(i, end=" ")


# time : O(n) + O(n+k) ~ O(n+k)
# space: O(k) due freq[]
