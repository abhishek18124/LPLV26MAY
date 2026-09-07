# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        ans = []

        def bfs() -> None:
            q = deque()
            q.append(root)
            q.append(None)

            while q:  # len(q) > 0
                cur = q.popleft()
                if cur is None:
                    if q:  # len(q) > 0
                        q.append(None)
                else:
                    # cur is reference to a TreeNode

                    # process the cur node
                    if q[0] is None:
                        ans.append(cur.val)
                    if cur.left is not None:
                        q.append(cur.left)
                    if cur.right is not None:
                        q.append(cur.right)

        bfs()

        return ans
