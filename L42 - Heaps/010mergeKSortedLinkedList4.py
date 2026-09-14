from typing import Optional, List
import heapq


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __lt__(self, other):
        return self.val < other.val


# time : O(nklogk)
# space: O(k) due to min_heap
class Solution:
    def mergeKLists(self, heads: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = []  # internal representation of the min_heap
        for head in heads:
            if head is not None:
                heapq.heappush(h, (head.val, head))

        dummy = ListNode()
        temp = dummy

        while h:
            _, min_node = heapq.heappop(h)
            temp.next = min_node
            temp = temp.next
            if min_node.next is not None:
                heapq.heappush(h, (min_node.next.val, min_node.next))

        return dummy.next


head1 = ListNode(1, ListNode(3, ListNode(5)))
head2 = ListNode(2, ListNode(4, ListNode(6)))

heads = [head1, head2]

s = Solution()
head = s.mergeKLists(heads)

while head is not None:
    print(head.val, end=" ")
    head = head.next
print()
