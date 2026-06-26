arr = [10, 20, 30, 40, 50]
n = len(arr)

# pSum = []
# for _ in range(n):
# 	pSum.append(None)

pSum = [None] * n

pSum[0] = arr[0]
for i in range(1, n):
    pSum[i] = pSum[i - 1] + arr[i]

print(pSum)
