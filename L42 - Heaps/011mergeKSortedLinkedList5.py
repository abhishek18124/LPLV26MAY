# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# time : O(nklogk)
# space: O(k) due to min_heap


def less_than(self, other):
    return self.val < other.val


class Solution:
    def mergeKLists(self, heads: List[Optional[ListNode]]) -> Optional[ListNode]:
        ListNode.__lt__ = less_than
        h = []  # internal representation of the min_heap
        for head in heads:
            if head is not None:
                heapq.heappush(h, head)

        dummy = ListNode()
        temp = dummy

        while h:
            min_node = heapq.heappop(h)
            temp.next = min_node
            temp = temp.next
            if min_node.next is not None:
                heapq.heappush(h, min_node.next)

        return dummy.next
