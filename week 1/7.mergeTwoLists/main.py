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
    def mergeTwoLists(self, list1: Node, list2: Node) -> LinkedList:
        ans = Node()
        current = ans
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next

            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        current.next = list1 or list2

        return ans.next


s = Solution()

l1 = LinkedList()
list1 = [1, 2, 4]
for i in list1:
    l1.append(i)
l1.print_list()

l2 = LinkedList()
list2 = [1, 3, 4]
for i in list2:
    l2.append(i)
l2.print_list()

s = Solution()
a = s.mergeTwoLists(l1.head, l2.head)
while a:
    print(a.val, end=" ")
    a = a.next
print()
