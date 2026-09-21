"""

********************************************
Implementation of DFS for Disconnected Graph
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
dfs(0): 0 2 5 3 1 4 6
dfs(7): 7 9 8 10 11
dfs(12): 12 13 15 14

"""


def dfs(u) -> None:  # u = current node
    # 1. mark the current node as visited
    vis[u] = True

    # 2. process the current node
    print(u, end=" ")

    # 3. explore all the neighbors of the current node
    for v in adj[u]:  # v = neighbor of current node
        if not vis[v]:  # neighbor is not visited
            # recursively visit the neighbor
            dfs(v)


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
        print(f"dfs({i}) = ", end=" ")
        dfs(i)
        cnt += 1
        print()

print(f"number of components = {cnt}")
