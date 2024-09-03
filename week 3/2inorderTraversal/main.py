# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recursiveInorderTraversal(self, root: TreeNode) -> list[int]:
        result = []

        if root:
            result += self.recursiveInorderTraversal(root.left)
            result.append(root.val)
            result += self.recursiveInorderTraversal(root.right)

        return result

    def iterativeInorderTraversal(self, root: TreeNode) -> list[int]:
        result = []
        stack = []
        current = root

        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            result.append(current.val)
            current = current.right

        return result



s = Solution()

root = TreeNode(3)
t1 = TreeNode(9)
t2 = TreeNode(20)
t3 = TreeNode(15)
t4 = TreeNode(7)
t5 = TreeNode(8)
t6 = TreeNode(4)

root.left = t1
root.right = t2
t2.left = t3
t2.right = t4
t1.right = t5
t1.left = t6

print(s.recursiveInorderTraversal(root=root))
print(s.iterativeInorderTraversal(root=root))
