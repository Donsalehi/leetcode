class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum = nums[0]
        sum = 0
        for num in nums:
            if sum < 0:
                sum = 0
            sum += num
            max_sum = max(max_sum, sum)
        return max_sum


s = Solution()
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(s.maxSubArray(nums))
