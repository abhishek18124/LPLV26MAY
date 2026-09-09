from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


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


# time : O(height of bst)


def insert_in_bst(root: TreeNode | None, key: int) -> TreeNode:
    # base case
    if root is None:
        return TreeNode(key)

    # recursive case
    if key < root.val:
        # ask your friend to insert the key in the left_subtree
        root.left = insert_in_bst(root.left, key)
    else:
        # key > root.val
        # ask your friendt to insert the key in the right_subtree
        root.right = insert_in_bst(root.right, key)

    return root


# time : O(height of the BST)


def search_in_bst(root: TreeNode | None, key: int) -> bool:
    # base case
    if root is None:
        return False

    # recursive case

    if root.val == key:
        return True
    elif key < root.val:
        # ask your friend to search for the key in the left_subtree
        return search_in_bst(root.left, key)
    else:
        # key > root.val
        # ask your friend to search for the key in the right_subtree
        return search_in_bst(root.right, key)


root = None  # tree is empty

root = insert_in_bst(root, 10)
root = insert_in_bst(root, 5)
root = insert_in_bst(root, 3)
root = insert_in_bst(root, 7)
root = insert_in_bst(root, 15)
root = insert_in_bst(root, 13)
root = insert_in_bst(root, 17)

key = 171

print(search_in_bst(root, key))
