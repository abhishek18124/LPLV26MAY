"""
********************************************
Implementation of Graph using Adjacency List
********************************************

input
5 6
0 1
0 2
1 3
2 3
2 4
3 4

"""

n, m = map(int, input().split())

adj = [[] for _ in range(n)]

for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)  # comment out this line of code if given graph is directed

for i in range(n):
    print(f"neighbors({i}) = {adj[i]}")
    # print("neighbors(", i, ") = ", *adj[i])
