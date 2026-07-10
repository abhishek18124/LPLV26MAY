from collections import Counter


def f(mid: int) -> bool:  # const
    # check if polycarpus can cook 'mid' no. of hamburgers
    eb = max(0, c["B"] * mid - nb)
    es = max(0, c["S"] * mid - ns)
    ec = max(0, c["C"] * mid - nc)

    return ((eb * pb) + (es * ps) + (ec * pc)) <= r


s = input()
nb, ns, nc = map(int, input().split())
pb, ps, pc = map(int, input().split())
r = int(input())

c = Counter(s)

lo = 0
hi = 10**12 + 100  # 1e12 + 100

ans = 0

while lo <= hi:  # log(hi-lo) # log(10^12) # 40 iterations
    mid = (lo + hi) // 2
    # can polycarpus cook 'mid' no. of hamburgers
    if f(mid):
        ans = mid
        lo = mid + 1
    else:
        hi = mid - 1

print(ans)
