"""
***********************************
SSSP for Unweighted Graph using BFS
***********************************

input
9 12
0  1
0  2
1  3
1  4
2  4
2  5
3  6
4  6
4  7
5  7
6  8
7  8

output
0 1 1 2 2 2 3 3 4
"""
from collections import deque


def bfs(src):
    vis[src] = True

    q = deque()
    q.append(src)

    while q:
        u = q.popleft()
        for v in adj[u]:
            if not vis[v]:
                vis[v] = True
                q.append(v)
                dist[v] = dist[u] + 1


n, m = map(int, input().split())

adj = [[] for _ in range(n)]

for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)  # comment out this line of code if given graph is directed

vis = [False] * n

INF = 1e9

dist = [INF] * n
src = 0

dist[src] = 0

bfs(src)

print(*dist)
