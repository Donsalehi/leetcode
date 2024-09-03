class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        total_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return total_sum - actual_sum


s = Solution()
nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
print(s.missingNumber(nums))
