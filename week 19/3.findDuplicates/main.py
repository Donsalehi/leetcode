class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        result = []

        for num in nums:
            index = abs(num) - 1

            if nums[index] > 0:
                nums[index] = -nums[index]
            else:
                result.append(abs(num))

        return result


s = Solution()
nums = [4, 3, 2, 7, 8, 2, 3, 1]
print(s.findDuplicates(nums))
