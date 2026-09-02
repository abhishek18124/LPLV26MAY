class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# time : O(n)
# space: O(height of binary tree) due to fn call stack


def print_in_order(root: TreeNode | None) -> None:
    # base case

    if root is None:
        # print(-1, end=" ")
        return

    # recursive case

    # f(root) : print the in_order of the given tree

    # 1. ask your friend to print the in_order of the left_subtree

    print_in_order(root.left)

    # 2. process the root node

    print(root.val, end=" ")

    # 3. ask your friend to print the in_order of the right_subtree

    print_in_order(root.right)


root = None  # tree is empty

root = TreeNode(10)

root.left = TreeNode(20)
root.right = TreeNode(30)

root.left.left = TreeNode(40)
root.left.right = TreeNode(50)
root.left.right.left = TreeNode(70)

root.right.right = TreeNode(60)

print_in_order(root)
