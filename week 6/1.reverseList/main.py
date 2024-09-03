class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, value):
        new_node = Node(val=value)

        if self.head is None:
            self.head = new_node
            return
        else:
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
    def reverseList(self, head: Node) -> Node:
        current = head
        previous = None
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous


head = [1, 2, 3, 4, 5]
l = LinkedList()
for i in head:
    l.append(i)
l.print_list()
s = Solution()
l.head = s.reverseList(l.head)
l.print_list()

