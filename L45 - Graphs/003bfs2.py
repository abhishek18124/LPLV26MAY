"""

********************************************
Implementation of BFS for Disconnected Graph
********************************************

input
16 16
0 2
0 3
1 3
1 4
2 5
3 5
3 6
4 6
7 9
8 9
9 10
9 11
12 13
12 14
13 15
14 15

output
bfs(0): 0 2 3 5 1 6 4
bfs(7): 7 9 8 10 11
bfs(12): 12 13 14 15

"""

from collections import deque


def bfs(src):
    vis[src] = True

    q = deque()
    q.append(src)

    while q:
        u = q.popleft()
        print(u, end=" ")
        for v in adj[u]:
            if not vis[v]:
                vis[v] = True
                q.append(v)


n, m = map(int, input().split())

adj = [[] for _ in range(n)]

for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)  # comment out this line of code if given graph is directed

vis = [False] * n

cnt = 0

for i in range(n):
    if not vis[i]:
        print(f"bfs({i}) = ", end=" ")
        bfs(i)
        cnt += 1
        print()

print(f"number of components = {cnt}")
