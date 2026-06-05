num = int(input())
ans = 0

while num != 0:
    d = num % 10
    ans = ans * 10 + d
    num = num // 10

print(ans)
