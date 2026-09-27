"""
***********************************
SSSP for Unweighted Graph using BFS
(With Path Reconstruction)
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
0 1 3 6 8

"""

from collections import deque


def bfs(src):
    q = deque()
    q.append(src)

    while q:
        u = q.popleft()
        for v in adj[u]:
            if dist[v] == INF:
                q.append(v)
                dist[v] = dist[u] + 1
                par[v] = u


n, m = map(int, input().split())

adj = [[] for _ in range(n)]

for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)  # comment out this line of code if given graph is directed

INF = 1e9

dist = [INF] * n
src = 0

par = [-1] * n
# par[src] = -1

dist[src] = 0

bfs(src)

# print(*dist)
# print(*par)

for i in range(n):
    print(f"dist({i}) = {dist[i]}")

print()

for i in range(n):
    print(f"par({i}) = {par[i]}")

dst = 8

# path reconstruction from the parent map

path = []
cur = dst
while par[cur] != -1:
    path.append(cur)
    cur = par[cur]
path.append(cur)

path.reverse()

print(*path)
