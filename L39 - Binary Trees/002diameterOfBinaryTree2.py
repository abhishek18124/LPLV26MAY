# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # time : O(n)

    def dfs(self, root: Optional[TreeNode]) -> int:
        # base case
        if root is None:
            return 0, -1

        # recursive case

        # f(root) : find the diameter of the given tree

        # 1. ask your friend to find the diameter of the left_subtree

        left_dia, left_hgt = self.dfs(root.left)

        # 2. ask your friend to find the diameter of the right_subtree

        right_dia, right_hgt = self.dfs(root.right)

        # 3. find the len of the longest path via the root node

        len_longest_path_via_root = left_hgt + right_hgt + 2

        return max(left_dia, right_dia, len_longest_path_via_root), 1 + max(
            left_hgt, right_hgt
        )

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dia, _ = self.dfs(root)
        return dia
