class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        n = len(nums)

        for i in range(n):
            index = abs(nums[i]) - 1
            if nums[index] > 0:
                nums[index] = -nums[index]

        return [i + 1 for i in range(n) if nums[i] > 0]


s = Solution()
nums = [4, 3, 2, 7, 8, 2, 3, 1]
print(s.findDisappearedNumbers(nums))
