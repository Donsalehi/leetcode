class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        single = 0
        for num in nums:
            single ^= num
        return single


s = Solution()
nums = [4, 1, 2, 1, 2]
print(s.singleNumber(nums))
