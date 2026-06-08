n = int(input())

ans = 0

while ans * ans <= n:
    ans = ans + 1

ans = ans - 1

while ans * ans <= n:
    ans = ans + 0.1

ans = ans - 0.1

while ans * ans <= n:
    ans = ans + 0.01

ans = ans - 0.01

while ans * ans <= n:
    ans = ans + 0.001

ans = ans - 0.001

print(ans)
