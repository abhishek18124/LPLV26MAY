"""
**************************************
Implementation of Dijkstra's Algorithm
(With Path Reconstruction)
**************************************

input
5 7
0 1 10
0 2 5
1 2 3
1 3 1
2 3 9
2 4 2
3 4 8

output
0 8 5 9 7
"""

import heapq
import math

n, m = map(int, input().split())

adj = [[] for _ in range(n)]

for _ in range(m):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))
    adj[v].append((u, w))  # comment out this line of code if given graph is directed

src = 0  # assume node 0 to be the source vertex

dist = [math.inf] * n  # distance array
dist[src] = 0

par = [-1] * n  # parent array

h = [(dist[src], src)]  # min_heap

while h:
    du, u = heapq.heappop(h)

    # lazy deletion: ignore stale distances

    if du > dist[u]:
        continue

    for v, w in adj[u]:
        if dist[v] > du + w:
            dist[v] = du + w
            heapq.heappush(h, (dist[v], v))
            par[v] = u

dst = 1

# Path Reconstruction

if dist[dst] == math.inf:
    print("no path exists")
else:
    path = []
    cur = dst

    while cur != -1:
        path.append(cur)
        cur = par[cur]

    path.reverse()

    print(*path)
