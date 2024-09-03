# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        first = second = dummy

        for _ in range(n + 1):
            first = first.next

        while first:
            first = first.next
            second = second.next

        second.next = second.next.next

        return dummy.next

    def removeNthFromEnd1(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        first = head
        length = 0

        while first:
            length += 1
            first = first.next

        length -= n
        first = dummy

        while length > 0:
            length -= 1
            first = first.next

        first.next = first.next.next

        return dummy.next


s = Solution()
head = ListNode(1)
l1 = ListNode(2)
l2 = ListNode(3)
l3 = ListNode(4)
l4 = ListNode(5)

head.next = l1
l1.next = l2
l2.next = l3
l3.next = l4

current = head

while current:
    print(current.val, end=" ")
    current = current.next
print()

new_head = s.removeNthFromEnd(head, 2)

current = new_head

while current:
    print(current.val, end=" ")
    current = current.next
print()

new_head1 = s.removeNthFromEnd1(head, 2)

current = new_head1

while current:
    print(current.val, end=" ")
    current = current.next
