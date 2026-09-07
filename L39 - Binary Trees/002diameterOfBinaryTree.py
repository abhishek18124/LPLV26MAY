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

    def dfs(self, root: Optional[TreeNode]) -> int:
        # base case
        if root is None:
            return 0

        # recursive case

        # f(root) : find the diameter of the given tree

        # 1. ask your friend to find the diameter of the left_subtree

        left_dia = self.dfs(root.left)

        # 2. ask your friend to find the diameter of the right_subtree

        right_dia = self.dfs(root.right)

        # 3. find the len of the longest path via the root node

        len_longest_path_via_root = (
            self.find_height(root.left) + self.find_height(root.right) + 2
        )

        return max(left_dia, right_dia, len_longest_path_via_root)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root)
