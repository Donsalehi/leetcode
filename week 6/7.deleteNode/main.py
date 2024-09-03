class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, val=0):
        new_node = Node(val)
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
    def deleteNode(self, node: Node):
        node.val = node.next.val
        node.next = node.next.next


s = Solution()
l = LinkedList()
head = [4, 5, 1, 9]
for i in head:
    l.append(i)
l.print_list()
s.deleteNode(l.head.next)
l.print_list()
