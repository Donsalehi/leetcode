# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == targetSum
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)


root = TreeNode(5)
t1 = TreeNode(4)
t2 = TreeNode(8)
t3 = TreeNode(11)
t4 = TreeNode(13)
t5 = TreeNode(4)
t6 = TreeNode(7)
t7 = TreeNode(2)
t8 = TreeNode(1)

root.left = t1
root.right = t2
t1.left = t3
t2.left = t4
t2.right = t5
t3.left = t6
t3.right = t7
t5.right = t8

s = Solution()
print(s.hasPathSum(root, 22))
