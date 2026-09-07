from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def build_tree_from_level_order():
    val = next(it)
    root = TreeNode(val)

    q = deque()
    q.append(root)

    while q:
        cur = q.popleft()
        val = next(it)
        if val != -1:
            cur.left = TreeNode(val)
            q.append(cur.left)

        val = next(it)
        if val != -1:
            cur.right = TreeNode(val)
            q.append(cur.right)

    return root


def print_level_order(root: TreeNode) -> None:
    q = deque()
    q.append(root)

    while q:  # len(q) > 0
        q_size = len(q)

        # process q_size nodes
        for _ in range(q_size):
            cur = q.popleft()
            # process the cur node
            print(cur.val, end=" ")
            if cur.left is not None:
                q.append(cur.left)
            if cur.right is not None:
                q.append(cur.right)

        print()


it = iter(map(int, input().split()))
root = None
root = build_tree_from_level_order()
print_level_order(root)
