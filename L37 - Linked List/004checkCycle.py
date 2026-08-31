from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s = set()

        while head is not None:
            if head in s:
                return True
            else:
                s.add(head)
                head = head.next

        return False


obj = Solution()

head = None
head = ListNode(10)
head.next = ListNode(20)
head.next.next = ListNode(30)
head.next.next.next = ListNode(40)
head.next.next.next.next = ListNode(50)
head.next.next.next.next.next = head.next

print(obj.hasCycle(head))
