class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, value):
        new_node = Node(value)
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
            print(current.value, end=" ")
            current = current.next
        print()


class Solution:
    def removeElements(self, head: Node, val: int) -> Node:
        dummy = Node(value=0, next=head)
        wanted = dummy
        while wanted.next:
            if wanted.next.value == val:
                temp = wanted.next
                wanted.next = wanted.next.next
                del temp

            else:
                wanted = wanted.next

        return dummy.next


head = [1, 2, 6, 3, 4, 5, 6]
val = 6
l = LinkedList()
for i in head:
    l.append(i)
l.print_list()
s = Solution()
l.head = s.removeElements(l.head, val)
l.print_list()


