# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode:
        if not nums:
            return None

        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])

        return root


def InOrder(tree: TreeNode):
    if tree.left:
        InOrder(tree.left)
    print(tree.val)
    if tree.right:
        InOrder(tree.right)


s = Solution()
nums = [-10, -3, 0, 5, 9]
root = s.sortedArrayToBST(nums)
InOrder(root)
