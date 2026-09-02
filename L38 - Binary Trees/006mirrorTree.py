class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def print_pre_order(root: TreeNode | None) -> None:
    # base case

    if root is None:
        # print(-1, end=" ")
        return

    # recursive case

    # f(root) : print the pre_order of the given tree

    # 1. process the root node

    print(root.val, end=" ")

    # 2. ask your friend to print the pre_order of the left_subtree

    print_pre_order(root.left)

    # 3. ask your friend to print the pre_order of the right_subtree

    print_pre_order(root.right)


# time : O(n)
# space: O(height of the binary tree) due to fn call stack


def dfs(root: TreeNode | None) -> None:
    # base case
    if root is None:
        return

    # recursive case

    # 1. ask your friend to mirror the left_subtree
    dfs(root.left)

    # 2. ask your friend to mirror the right_subtree
    dfs(root.right)

    # 3. swap the left_child and right_child of the root node
    root.left, root.right = root.right, root.left


root = None  # tree is empty

root = TreeNode(10)

root.left = TreeNode(20)
root.right = TreeNode(30)

root.left.left = TreeNode(40)
root.left.right = TreeNode(50)
root.left.right.left = TreeNode(70)

root.right.right = TreeNode(60)

print_pre_order(root)

print()

dfs(root)

print_pre_order(root)
