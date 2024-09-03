# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        current = head
        carry = 0

        while l1 or l2 or carry:
            sum_ = carry
            if l1:
                sum_ += l1.val
                l1 = l1.next
            if l2:
                sum_ += l2.val
                l2 = l2.next
            carry, val = divmod(sum_, 10)
            current.next = ListNode(val)
            current = current.next
        return head.next


def insert(l: list):
    head = ListNode(l[0])
    current = head
    for i in range(1, len(l)):
        current.next = ListNode(int(l[i]))
        current = current.next
    return head


s = Solution()
l1 = [9, 9, 9, 9, 9, 9, 9]
l2 = [9, 9, 9, 9]
h1 = insert(l1)
h2 = insert(l2)
current = s.addTwoNumbers(h1, h2)
while current:
    print(current.val, end="")
    current = current.next
