# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # time : O(n)
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        prev = head
        cur = head.next

        while cur is not None:
            if cur.val == prev.val:
                # skip the cur node
                cur = cur.next
            else:
                # track the cur node
                prev.next = cur
                prev = cur
                cur = cur.next

        prev.next = None
        return head
