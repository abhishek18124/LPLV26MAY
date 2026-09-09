# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def find_minimum(root: TreeNode) -> int:
            if root is None:
                return float("inf")

            while root.left is not None:
                root = root.left

            return root.val

        def find_maximum(root: TreeNode) -> int:
            if root is None:
                return float("-inf")

            while root.right is not None:
                root = root.right

            return root.val

        def dfs(root: TreeNode) -> bool:
            # base case
            if root is None:
                return True

            # recursive case

            # f(root) : check if the given tree is a bst

            # 1. ask your friend to check if the left_subtree is a bst
            left_is_bst = dfs(root.left)

            # 2. ask your friend to check if the right_subtree is a bst
            right_is_bst = dfs(root.right)

            # 3. check if the bst prop. works at root
            does_bst_prop_work_at_root = root.val > find_maximum(
                root.left
            ) and root.val < find_minimum(root.right)

            return left_is_bst and right_is_bst and does_bst_prop_work_at_root

        return dfs(root)
