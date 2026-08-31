# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def print_linked_list(head: ListNode) -> None:
    while head:
        print(head.val, end=" ")
        head = head.next
    print()


# time : O(n)
# space: O(1)


def remove_cycle(head: ListNode) -> None:
    slow = head
    fast = head

    while True:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            break

    # at present, slow and fast are at the meeting point

    prev = head
    while prev.next is not slow:
        prev = prev.next

    # at present, prev is one-step behind the meeting point

    slow = head

    while slow is not fast:
        slow = slow.next
        fast = fast.next
        prev = prev.next

    # at present, slow and fast are the start of the cycle and therefore prev is at the tail node
    prev.next = None


head = None
head = ListNode(10)
head.next = ListNode(20)
head.next.next = ListNode(30)
head.next.next.next = ListNode(40)
head.next.next.next.next = ListNode(50)
head.next.next.next.next.next = head.next

remove_cycle(head)

print_linked_list(head)
