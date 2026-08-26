from typing import Optional


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


# time : O(n)
# space: O(n) due to fn call stack


def find_length_recursive(head: ListNode) -> int:
    # base case
    if head is None:
        # f(None) : find the length of an empty linkedList
        return 0

    # recursive case

    # f(head) : find the length of the given linkedList

    # 1. ask your friend to find the length of the linkedList that starts from the node which comes after the head node
    x = find_length_recursive(head.next)

    # 2. use the answer from your friend to solve the given problem
    return 1 + x


head = None
head = ListNode(10)
head.next = ListNode(20)
head.next.next = ListNode(30)
head.next.next.next = ListNode(40)
head.next.next.next.next = ListNode(50)

print(find_length_recursive(head))
