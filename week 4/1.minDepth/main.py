# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        if not root.left:
            return 1 + self.minDepth(root.right)

        if not root.right:
            return 1 + self.minDepth(root.left)

        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

    def minDepth2(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = [root]
        min_depth = 0
        while queue:
            size = len(queue)
            min_depth += 1
            for _ in range(size):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if not node.left and not node.right:
                    return min_depth


# return min_depth???


s = Solution()

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

root2 = TreeNode(2)
root2.left = TreeNode(3)
root2.left.left = TreeNode(4)
root2.left.left.left = TreeNode(5)
root2.left.left.left.left = TreeNode(6)

print(s.minDepth(root))
print(s.minDepth(root2))
print(s.minDepth2(root))
print(s.minDepth2(root2))
