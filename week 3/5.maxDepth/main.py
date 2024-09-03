# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def maxDepth2(self, root: TreeNode) -> int:
        stack = []
        result = 0
        if root:
            stack.append((root, 1))
        while stack:
            node, depth = stack.pop()
            result = max(result, depth)
            if node.left:
                stack.append((node.left, depth+1))
            if node.right:
                stack.append((node.right, depth+1))
        return result


s = Solution()

root = TreeNode(3)
t1 = TreeNode(9)
t2 = TreeNode(20)
t3 = TreeNode(15)
t4 = TreeNode(7)
t5 = TreeNode(8)
t6 = TreeNode(4)
t7 = TreeNode(6)

root.left = t1
root.right = t2
t2.left = t3
t2.right = t4
t1.right = t5
t1.left = t6
t3.left = t7

print(s.maxDepth(root))
print(s.maxDepth2(root))
