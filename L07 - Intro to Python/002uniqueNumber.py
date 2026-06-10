n = int(input())

ans = 0
for _ in range(n):
    x = int(input())
    ans = ans ^ x

print(ans)
