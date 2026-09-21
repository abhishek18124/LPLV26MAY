"""

*****************************************
Implementation of DFS for Connected Graph
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
0 1 3 6 4 2 5 7 8

"""

# n : number of nodes
# m : number of edges

# time : n.const + 2m.const ~ O(n + 2m) or O(V + 2E)
# space: n due to vis[] + n due to fn call stack ~ O(n) or O(V)


def dfs(u):  # u = current node
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

dfs(0)
