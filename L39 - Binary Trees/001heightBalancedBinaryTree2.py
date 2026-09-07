# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # time : O(n)
    # space: O(height of binary tree) due to fn call stack
    def dfs(self, root: Optional[TreeNode]) -> tuple:
        # base case
        if root is None:
            return True, -1

        # recursive case

        # 1. ask your friend to check if the left_subtree is height_balanced and simultaneously find the height of the left_subtree

        left_is_bal, left_hgt = self.dfs(root.left)

        # 2. ask your friend to check if the right_subtree is height_balanced and simultaneously find the height of the right_subtree

        right_is_bal, right_hgt = self.dfs(root.right)

        # 3. check if the height-balance prop. works at root
        does_hb_prop_work_at_root = abs(left_hgt - right_hgt) <= 1

        return left_is_bal and right_is_bal and does_hb_prop_work_at_root, 1 + max(
            left_hgt, right_hgt
        )

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        is_bal, _ = self.dfs(root)
        return is_bal
