# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# time : O(nklogk)
# space: O(k) due to min_heap
class Solution:
    def mergeKLists(self, heads: List[Optional[ListNode]]) -> Optional[ListNode]:
        unique_id = 0

        h = []  # internal representation of the min_heap
        for head in heads:
            if head is not None:
                heapq.heappush(h, (head.val, unique_id, head))
                unique_id += 1

        dummy = ListNode()
        temp = dummy

        while h:
            _, _, min_node = heapq.heappop(h)
            temp.next = min_node
            temp = temp.next
            if min_node.next is not None:
                heapq.heappush(h, (min_node.next.val, unique_id, min_node.next))
                unique_id += 1

        return dummy.next
