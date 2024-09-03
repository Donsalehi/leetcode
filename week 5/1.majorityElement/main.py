class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        n = len(nums)
        edge = n // 2
        values = set(nums)
        for i in values:
            if nums.count(i) > edge:
                solution = i
                break
        return solution


s = Solution()
nums = [2, 2, 1, 1, 1, 2, 2]
print(s.majorityElement(nums))