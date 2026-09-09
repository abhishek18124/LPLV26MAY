# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # time : O(n)
        def dfs(root: TreeNode | None) -> tuple:
            # base case
            if root is None:
                return True, float("inf"), float("-inf")

            # recursive case

            left_is_bst, left_minval, left_maxval = dfs(root.left)
            right_is_bst, right_minval, right_maxval = dfs(root.right)

            # 3. check if the bst prop. works at root
            does_bst_prop_work_at_root = (
                root.val > left_maxval and root.val < right_minval
            )

            return (
                left_is_bst and right_is_bst and does_bst_prop_work_at_root,
                min(root.val, left_minval, right_minval),
                max(root.val, left_maxval, right_maxval),
            )

        is_bst, _, _ = dfs(root)
        return is_bst
