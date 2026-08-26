from typing import Optional


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


# time : O(1)
def insert_at_head(head: Optional[ListNode], val: int) -> ListNode:
    n = ListNode(val)
    n.next = head
    return n


# # time : O(1)
# def insert_at_head(head: ListNode | None, val: int) -> ListNode:
#     n = ListNode(val)
#     n.next = head
#     return n


# time : O(n)
def print_linked_list(head: ListNode | None) -> None:
    while head:
        print(head.val, end=" ")
        head = head.next
    print()


# time : O(1)
def delete_at_head(head: ListNode | None) -> ListNode | None:
    if head is None:
        # linkedList is empty
        return head  # return None

    # linkedList is non-empty
    return head.next


def get_tail(head: ListNode) -> ListNode:
    while head.next is not None:
        head = head.next
    return head


# time : O(n)


def insert_at_tail(head: ListNode | None, val: int) -> ListNode:
    if head is None:
        # linkedList is empty

        # head = ListNode(val)
        # return head

        return ListNode(val)

    # linkedList is non-empty
    n = ListNode(val)
    tail = get_tail(head)
    tail.next = n

    return head


# time : O(n)


def delete_at_tail(head: ListNode | None) -> ListNode | None:
    if head is None:
        # linkedList is empty
        return head

    # linkedList is non-empty

    if head.next is None:
        # linkedList has exactly one node
        head = None
        return head

    # linkedList has >= 2 nodes

    prev = None
    cur = head

    while cur.next is not None:
        prev = cur
        cur = cur.next

    prev.next = None
    return head


head = None
head = ListNode(10)
head.next = ListNode(20)
head.next.next = ListNode(30)
head.next.next.next = ListNode(40)
head.next.next.next.next = ListNode(50)

print_linked_list(head)

head = delete_at_tail(head)

print_linked_list(head)
