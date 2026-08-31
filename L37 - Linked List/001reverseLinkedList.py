class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def insert_at_head(head: ListNode, val: int) -> ListNode:
    n = ListNode(val)
    n.next = head
    return n


def print_linked_list(head: ListNode) -> None:
    while head:
        print(head.val, end=" ")
        head = head.next
    print()


# time : O(n)
# space: O(1)


def reverse_linked_list(head: ListNode | None) -> ListNode | None:
    prev = None
    cur = head

    while cur is not None:
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp

    return prev


head = None

head = insert_at_head(head, 50)
head = insert_at_head(head, 40)
head = insert_at_head(head, 30)
head = insert_at_head(head, 20)
head = insert_at_head(head, 10)

print_linked_list(head)  # 10 20 30 40 50

head = reverse_linked_list(head)

print_linked_list(head)  # 50 40 30 20 10
