"""

*****************************************
Implementation of BFS for Connected Graph
*****************************************

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
0 1 2 3 4 5 6 7 8

"""

from collections import deque

# time : n.const + 2m.const ~ O(n + 2m) or O(V + 2E)
# space: O(n) or O(V)


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

bfs(0)
