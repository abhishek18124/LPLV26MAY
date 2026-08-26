class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


n1 = ListNode(10)
print(n1.val)
print(n1.next)

n2 = ListNode(20)
print(n2.val)
print(n2.next)

n1.next = n2
