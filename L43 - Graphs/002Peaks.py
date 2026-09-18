n, m = map(int, input().split())
h = list(map(int, input().split()))
adj = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1  # converts 1-based input into 0-based
    v -= 1  # converts 1-based input into 0-based
    adj[u].append(v)
    adj[v].append(u)  # comment out this line of code if given graph is directed

cnt = 0

for u in range(n):
    # check if the observatory corresponding to node u is good ?

    flag = True  # assume observatory corresponding to node u is good

    for v in adj[u]:
        if h[v] >= h[u]:
            flag = False
            break

    if flag:
        cnt += 1

print(cnt)

# time : O(n + 2m) or O(V + 2E)
# space: O(n + 2m) or O(V + 2E)
