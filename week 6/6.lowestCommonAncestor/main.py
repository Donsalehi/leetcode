class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BST:
    def __init__(self, root=None):
        self.root = root

    def insert(self, val=0):
        if self.root is None:
            self.root = Node(val)
        else:
            self._insert_node(self.root, val)

    def _insert_node(self, node, val):
        if val is None:
            return
        if val < node.val:
            if node.left is None:
                node.left = Node(val)
            else:
                self._insert_node(node.left, val)
        else:
            if node.right is None:
                node.right = Node(val)
            else:
                self._insert_node(node.right, val)


class Solution:
    def lowestCommonAncestor(self, root: Node, p: Node, q: Node) -> int:
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root.val


b = BST()
keys = root = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
for key in keys:
    b.insert(key)
s = Solution()
print(s.lowestCommonAncestor(b.root, Node(2), Node(4)))
