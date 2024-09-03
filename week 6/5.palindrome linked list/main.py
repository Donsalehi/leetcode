class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, value=0):
        new_node = Node(val=value)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.val, end=" ")
            current = current.next
        print()


class Solution:
    def isPalindrom(self, head:Node) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        while prev:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next

        return True


s = Solution()
l = LinkedList()
head = [1, 2, 2, 1]
for i in head:
    l.append(i)
print(s.isPalindrom(l.head))
