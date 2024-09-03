# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False

        tortoise = head
        hare = head.next

        while tortoise != hare:
            if not hare or not hare.next:
                return False
            tortoise = tortoise.next
            hare = hare.next.next

        return True


head = ListNode(3)
n1 = ListNode(2)
n2 = ListNode(0)
n3 = ListNode(-4)

head.next = n1
n1.next = n2
n2.next = n3
n3.next = n1

s = Solution()
print(s.hasCycle(head))
