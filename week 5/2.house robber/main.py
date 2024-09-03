class Solution:
    def rob(self, nums: list[int]) -> int:
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        profit = [0] * len(nums)
        profit[0] = nums[0]
        profit[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            profit[i] = max(profit[i - 1], profit[i - 2] + nums[i])

        return profit[-1]


s = Solution()
nums = [2, 7, 9, 3, 1]
result = s.rob(nums)
print(f"Maximum amount that can be robbed: {result}")
