# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        ptrA = headA
        ptrB = headB

        while ptrA != ptrB:
            ptrA = headB if not ptrA else ptrA.next
            ptrB = headA if not ptrB else ptrB.next

        return ptrA


headA = ListNode(4)
n1 = ListNode(1)
n2 = ListNode(8)
n3 = ListNode(4)
n4 = ListNode(5)

headA.next = n1
n1.next = n2
n2.next = n3
n3.next = n4

headB = ListNode(5)
m1 = ListNode(6)
m2 = ListNode(1)

headB.next = m1
m1.next = m2
m2.next = n2

s = Solution()
answer = s.getIntersectionNode(headA, headB)
print(answer.val)
