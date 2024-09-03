class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        unique_index = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[unique_index]:
                unique_index += 1
                nums[unique_index] = nums[i]
        return unique_index + 1


s = Solution()
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(s.removeDuplicates(nums))
print(nums)
