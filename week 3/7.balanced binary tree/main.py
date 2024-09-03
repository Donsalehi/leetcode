# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def depth(root: TreeNode):
            if not root:
                return 0
            return 1 + max(depth(root.left), depth(root.right))

        if not root:
            return True
        if not root.left and not root.right:
            return True

        return (abs(depth(root.left) - depth(root.right)) <= 1) and (self.isBalanced(root.left)) and (self.isBalanced(root.right))

    def isBalanced2(self, root: TreeNode) -> bool:
        def dfs(root):
            if not root:
                return [True, 0]
            left, right = dfs(root.left), dfs(root.right)
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            return [balanced, 1 + max(left[1], right[1])]
        return dfs(root)[0]


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

print(s.isBalanced(root))
print(s.isBalanced2(root))
