from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# time : O(n)
# space: O(n) due to queue


def print_level_order(root: TreeNode) -> None:
    q = deque()
    q.append(root)
    q.append(None)

    while q:  # len(q) > 0
        cur = q.popleft()
        if cur is None:
            print()
            if q:  # len(q) > 0
                q.append(None)
        else:
            # cur is reference to a TreeNode

            # process the cur node
            print(cur.val, end=" ")
            if cur.left is not None:
                q.append(cur.left)
            if cur.right is not None:
                q.append(cur.right)


root = None  # tree is empty

root = TreeNode(10)

root.left = TreeNode(20)
root.right = TreeNode(30)

root.left.left = TreeNode(40)
root.left.right = TreeNode(50)
root.left.right.left = TreeNode(70)

root.right.right = TreeNode(60)

print_level_order(root)
