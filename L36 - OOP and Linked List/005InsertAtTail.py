class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


# time : O(1)
def insert_at_head(head: ListNode, val: int) -> ListNode:
    n = ListNode(val)
    n.next = head
    return n


# time : O(n)
def print_linked_list(head: ListNode) -> None:
    while head:
        print(head.val, end=" ")
        head = head.next
    print()


# time : O(1)
def delete_at_head(head: ListNode) -> ListNode:
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


def insert_at_tail(head: ListNode, val: int) -> ListNode:
    if head is None:
        # linkedList is empty

        # head = ListNode(val)
        # return head

        return ListNode(val)

    n = ListNode(val)
    tail = get_tail(head)
    tail.next = n

    return head


head = None
head = ListNode(10)
head.next = ListNode(20)
head.next.next = ListNode(30)
head.next.next.next = ListNode(40)
head.next.next.next.next = ListNode(50)

print_linked_list(head)

head = insert_at_tail(head, 60)

print_linked_list(head)
