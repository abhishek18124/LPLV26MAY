n = int(input())
p = int(input())

ans = 0

while ans * ans <= n:
    ans = ans + 1

ans = ans - 1

inc_fac = 0.1

for _ in range(p):
    while ans * ans <= n:
        ans = ans + inc_fac
    ans = ans - inc_fac
    inc_fac = inc_fac / 10

print(round(ans, p))

# print(f"{ans:.4f}")
