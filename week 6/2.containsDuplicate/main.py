class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


s = Solution()
nums = [1, 2, 3, 1]
print(s.containsDuplicate(nums))
