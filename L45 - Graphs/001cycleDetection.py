"""

**************************************
Cycle Detection in an Undirected Graph
**************************************

input
3 3
0 1
0 2
1 2

output
true

"""

# time : O(V + 2E) or O(n + 2m)
# space: O(V) or O(n)


def dfs(u, par) -> bool:  # u = current node
    # 1. mark the current node as visited
    vis[u] = True

    # 2. explore the neighbors of current node
    for v in adj[u]:  # v = neighbor of current node
        if not vis[v]:
            if dfs(v, u):
                return True
        else:
            # check if edge b/w u and v is a backedge
            if v != par:
                # the edge b/w u and v is a backedge
                return True

    return False


n, m = map(int, input().split())

adj = [[] for _ in range(n)]

for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)  # comment out this line of code if given graph is directed

flag = False  # assume given graph is acyclic
vis = [False] * n

for i in range(n):
    if not vis[i]:
        if dfs(i, -1):
            flag = True
            break

if flag:
    print("cycle found")
else:
    print("cycle not found")
