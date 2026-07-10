def f(mid: float) -> bool:
    # check if we can cut >= k pieces of length mid from n ropes
    cnt = 0

    for rope_len in a:
        cnt += rope_len // mid

    return cnt >= k


n, k = map(int, input().split())
a = [int(input()) for _ in range(n)]

lo = 0.0
hi = 1e7

for _ in range(60):
    mid = (lo + hi) / 2
    if f(mid):
        lo = mid
    else:
        hi = mid

print(f"{lo:.7f}")
