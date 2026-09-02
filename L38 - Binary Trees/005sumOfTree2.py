class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# time : O(n)
# space: O(height of the binary tree) due to fn call stack
def dfs(root: TreeNode | None) -> int:
    # base case
    if root is None:
        # tree is empty
        return 0

    # recursive case

    # f(root) : find the sum of the given tree

    # 1. ask your friend to find the sum of the leftSubtree
    left_sum = dfs(root.left)

    # 2. ask your friend to find the sum of the rightSubtree
    right_sum = dfs(root.right)

    # 3. use answers from your friend to get the final answer
    return left_sum + right_sum + root.val


root = None  # tree is empty

root = TreeNode(10)

root.left = TreeNode(20)
root.right = TreeNode(30)

root.left.left = TreeNode(40)
root.left.right = TreeNode(50)
root.left.right.left = TreeNode(70)

root.right.right = TreeNode(60)

print(dfs(root))
