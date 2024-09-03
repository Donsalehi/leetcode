# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


s = Solution()

p = TreeNode(1)
t1 = TreeNode(2)
t2 = TreeNode(3)

q = TreeNode(1)
t3 = TreeNode(2)
t4 = TreeNode(3)

p.left = t1
p.right = t2

q.left = t3
q.right = t4

print(s.isSameTree(p, q))
