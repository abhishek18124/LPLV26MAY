"""
https://leetcode.com/problems/is-graph-bipartite/description/
"""


class Solution:
    def isBipartite(self, adj: list[list[int]]) -> bool:
        def bfs(src) -> bool:
            color[src] = 0
            q = deque()
            q.append(src)

            while q:
                u = q.popleft()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        q.append(v)
                    else:
                        if color[u] == color[v]:
                            return False

            return True

        n = len(adj)
        color = [-1] * n

        for i in range(n):
            if color[i] == -1:
                if bfs(i) == False:
                    return False

        return True
