from itertools import count

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# time : O(nklogk)
# space: O(k) due to min_heap


class Solution:
    def mergeKLists(self, heads: List[Optional[ListNode]]) -> Optional[ListNode]:
        unique_id = count()

        h = []  # internal representation of the min_heap
        for head in heads:
            if head is not None:
                heapq.heappush(h, (head.val, next(unique_id), head))

        dummy = ListNode()
        temp = dummy

        while h:
            _, _, min_node = heapq.heappop(h)
            temp.next = min_node
            temp = temp.next
            if min_node.next is not None:
                heapq.heappush(h, (min_node.next.val, next(unique_id), min_node.next))

        return dummy.next
