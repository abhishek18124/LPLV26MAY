# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse_linked_list(self, head: ListNode | None) -> ListNode | None:
        prev = None
        cur = head

        while cur is not None:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        return prev

    def find_mid_point(self, head: ListNode | None) -> ListNode | None:
        if head is None:
            # linkedList is empty
            return head

        slow = head
        fast = head.next

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # 1. find the mid_point of the given linked_list

        mid_point = self.find_mid_point(head)

        # 2. split the given linked_list around the mid_point

        head2 = mid_point.next
        mid_point.next = None

        # 3. reverse the 2nd half of the given linked_list

        head2 = self.reverse_linked_list(head2)

        # 4. compare both the halves

        while head2 is not None:
            if head.val != head2.val:
                return False

            # head.val is equal to head2.val
            head = head.next
            head2 = head2.next

        return True  # given linkedList is a palindrome
