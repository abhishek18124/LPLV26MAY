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


def find_minimum(root: TreeNode | None) -> TreeNode:
    if root is None:
        return root

    while root.left is not None:
        root = root.left

    return root


def find_maximum(root: TreeNode | None) -> TreeNode:
    if root is None:
        return root

    while root.right is not None:
        root = root.right

    return root


# time : O(height of BST)


def delete_from_bst(root: TreeNode | None, key: int) -> TreeNode:
    # base case
    if root is None:
        return root

    # recursive case

    if key < root.val:
        # ask your friend to delete the key, if present, from the left_subtree
        root.left = delete_from_bst(root.left, key)
    elif key > root.val:
        # ask your friend to delete the key, if present, from the right_subtree
        root.right = delete_from_bst(root.right, key)
    else:
        # key is equal to root.val therefore delete root
        if root.left is None and root.right is None:
            # leaf node
            root = None
        elif root.left is None and root.right is not None:
            # node with a single right child
            root = root.right
        elif root.left is not None and root.right is None:
            # node with a single left child
            root = root.left
        else:
            # node with a two child nodes

            # left_max = find_maximum(root.left)
            # root.val, left_max.val = left_max.val, root.val
            # root.left = delete_from_bst(root.left, key)

            right_min = find_minimum(root.right)
            root.val, right_min.val = right_min.val, root.val
            root.right = delete_from_bst(root.right, key)

    return root


root = None  # tree is empty

root = insert_in_bst(root, 10)
root = insert_in_bst(root, 5)
root = insert_in_bst(root, 3)
root = insert_in_bst(root, 7)
root = insert_in_bst(root, 6)
root = insert_in_bst(root, 9)
root = insert_in_bst(root, 15)
root = insert_in_bst(root, 13)
root = insert_in_bst(root, 17)

print_in_order(root)

print()

print_level_order(root)

print()

key = 3

root = delete_from_bst(root, key)

print_in_order(root)

print()

print_level_order(root)

print()

key = 5

root = delete_from_bst(root, key)

print_in_order(root)

print()

print_level_order(root)

print()

key = 10

root = delete_from_bst(root, key)

print_in_order(root)

print()

print_level_order(root)

print()
