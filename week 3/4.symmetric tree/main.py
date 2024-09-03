# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        q = [root.left, root.right]

        while q:
            left_node = q.pop(0)
            right_node = q.pop(0)
            if not left_node and not right_node:
                continue
            if not left_node or not right_node:
                return False
            if left_node.val != right_node.val:
                return False
            q.append(left_node.left)
            q.append(right_node.right)
            q.append(left_node.right)
            q.append(right_node.left)

        return True

    def isSymmetric2(self, root: TreeNode) -> bool:
        def isMirror(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            return (left.val == right.val) and (isMirror(left.left, right.right)) and (isMirror(left.right, right.left))
        return isMirror(root.left, root.right)


s = Solution()

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)


print(s.isSymmetric(root))
print(s.isSymmetric2(root))
