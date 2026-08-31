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


# time : n/2.const ~ O(n)
# space: O(1)


def find_mid_point(head: ListNode | None) -> ListNode | None:
    if head is None:
        # linkedList is empty
        return head

    slow = head
    fast = head.next

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow


head = None

head = insert_at_head(head, 60)
head = insert_at_head(head, 50)
head = insert_at_head(head, 40)
head = insert_at_head(head, 30)
head = insert_at_head(head, 20)
head = insert_at_head(head, 10)

mid_point = find_mid_point(head)

if mid_point is not None:
    print(mid_point.val)  # 30
else:
    print("linkedList is empty")
