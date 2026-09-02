class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


total_sum = 0


def dfs(root: TreeNode | None) -> None:
    global total_sum

    # base case
    if root is None:
        return

    # recursive case

    total_sum += root.val
    dfs(root.left)
    dfs(root.right)


root = None  # tree is empty

root = TreeNode(10)

root.left = TreeNode(20)
root.right = TreeNode(30)

root.left.left = TreeNode(40)
root.left.right = TreeNode(50)
root.left.right.left = TreeNode(70)

root.right.right = TreeNode(60)

dfs(root)

print(total_sum)
