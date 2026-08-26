from typing import Optional


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


# time : O(n)
# space: O(1)


def find_length(head: ListNode | None) -> int:
    cnt = 0
    while head is not None:
        cnt += 1
        head = head.next
    return cnt


head = None
head = ListNode(10)
head.next = ListNode(20)
head.next.next = ListNode(30)
head.next.next.next = ListNode(40)
head.next.next.next.next = ListNode(50)

print(find_length(head))
