# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(
        self, head1: Optional[ListNode], head2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()
        temp = dummy

        while head1 is not None and head2 is not None:
            if head1.val <= head2.val:
                temp.next = head1
                temp = temp.next
                head1 = head1.next
            else:
                temp.next = head2
                temp = temp.next
                head2 = head2.next

        if head1 is not None:
            temp.next = head1
        else:
            temp.next = head2

        return dummy.next
