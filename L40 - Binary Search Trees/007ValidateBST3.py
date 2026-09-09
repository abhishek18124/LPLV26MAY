# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # time : O(n)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root: TreeNoode, lb: float, ub: float) -> bool:
            # base case
            if root is None:
                return True

            # recursive case

            return (
                root.val > lb
                and root.val < ub
                and dfs(root.left, lb, root.val)
                and dfs(root.right, root.val, ub)
            )

        lb = float("-inf")
        ub = float("inf")

        return dfs(root, lb, ub)
