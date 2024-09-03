class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return left


s = Solution()
nums = [1, 3, 5, 6]
print(s.searchInsert(nums, 2))
print(s.searchInsert(nums, 5))
print(s.searchInsert(nums, 7))
