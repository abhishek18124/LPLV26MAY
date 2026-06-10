n = int(input())
k = int(input())

mask = 1 << k
ans = n ^ mask

print(ans)
