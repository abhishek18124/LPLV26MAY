class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


# # time : O(1)
# def insert_at_head(head: ListNode, val: int) -> ListNode:
#     n = ListNode(val)
#     n.next = head
#     head = n
#     return head


# time : O(1)
def insert_at_head(head: ListNode, val: int) -> ListNode:
    n = ListNode(val)
    n.next = head
    return n


# # time : O(n)
# def print_linked_list(head: ListNode) -> None:
#     while head is not None:
#         print(head.val, end=" ")
#         head = head.next
#     print()


# time : O(n)
def print_linked_list(head: ListNode) -> None:
    while head:
        print(head.val, end=" ")
        head = head.next
    print()


head = None
head = ListNode(10)
head.next = ListNode(20)
head.next.next = ListNode(30)
head.next.next.next = ListNode(40)
head.next.next.next.next = ListNode(50)

print_linked_list(head)

head = insert_at_head(head, 0)

print_linked_list(head)
