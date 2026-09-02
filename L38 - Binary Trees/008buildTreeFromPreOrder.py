class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def print_pre_order(root: TreeNode | None) -> None:
    # base case

    if root is None:
        print(-1, end=" ")
        return

    # recursive case

    # f(root) : print the pre_order of the given tree

    # 1. process the root node

    print(root.val, end=" ")

    # 2. ask your friend to print the pre_order of the left_subtree

    print_pre_order(root.left)

    # 3. ask your friend to print the pre_order of the right_subtree

    print_pre_order(root.right)


def dfs(it) -> TreeNode:
    val = next(it)

    if val == -1:
        return None

    root = TreeNode(val)

    # 1. ask your friend to construct the left_subtree from its pre_order

    root.left = dfs(it)

    # 2. ask your friend to construct the right_subtree from its pre_order

    root.right = dfs(it)

    return root


it = iter(map(int, input().split()))
root = dfs(it)
print_pre_order(root)
