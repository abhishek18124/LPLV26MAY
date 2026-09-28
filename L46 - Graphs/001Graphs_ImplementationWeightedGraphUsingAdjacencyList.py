"""
*****************************************************
Implementation of Weighted Graph using Adjacency List
*****************************************************

input

5 6
0 1 7
0 2 1
1 3 2
2 3 9
2 4 6
3 4 5

"""

n, m = map(int, input().split())

adj = [[] for _ in range(n)]

for _ in range(m):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))
    adj[v].append((u, w))  # comment out this line of code if given graph is directed

for i in range(n):
    print(f"neighbors({i}) :", end=" ")
    for v, w in adj[i]:
        print(f"({v}, {w})", end=" ")
    print()
