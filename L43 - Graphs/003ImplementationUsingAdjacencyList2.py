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

from collections import defaultdict

n, m = map(int, input().split())
adj = defaultdict(list)
for _ in range(m):
    u, v = input().split()
    adj[u].append(v)
    adj[v].append(u)


for k, v in adj.items():
    print(k, v)
