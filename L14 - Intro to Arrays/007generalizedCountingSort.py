n, l, r = map(int, input().split())
arr = list(map(int, input().split()))

freq = [0] * (r - l + 1)
# time : O(n)
for x in arr:
    freq[x - l] += 1


# time : O(n + (r - l + 1)) ~ O(n + (r-l))
for i in range(r - l + 1):
    # print 'i+l' freq[i] times
    for _ in range(freq[i]):
        print(i + l, end=" ")


# time : O(n) + O(n + (r-l)) ~ O(n + (r-l))
# space: O(r-l+1) due freq[] ~ O(r-l)
