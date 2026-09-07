# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find_height(self, root: Optional[TreeNode]) -> int:
        # base case
        if root is None:
            return -1

        # recursive case

        # find_height(root) : find the height of the given tree

        # 1. ask your friend to find the height of the leftSubtree
        left_hgt = self.find_height(root.left)

        # 2. ask your friend to find the height of the rightSubtree
        right_hgt = self.find_height(root.right)

        return 1 + max(left_hgt, right_hgt)

    # time : O(n^2)

    def dfs(self, root: Optional[TreeNode]) -> bool:
        # base case
        if root is None:
            return True

        # recursive case

        # f(root) : check if the given tree is height-balanced or not

        # 1. ask your friend to check if the leftSubtree is height-balanced
        left_is_bal = self.dfs(root.left)

        # 2. ask your friend to check if the rightSubtree is height-balanced
        right_is_bal = self.dfs(root.right)

        # 3. check if the height-balance prop. works at root
        does_hb_prop_work_at_root = (
            abs(self.find_height(root.left) - self.find_height(root.right)) <= 1
        )

        return left_is_bal and right_is_bal and does_hb_prop_work_at_root

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root)
