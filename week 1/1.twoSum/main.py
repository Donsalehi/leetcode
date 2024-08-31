class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_dict = dict()
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                return [num_dict[complement], i]
            num_dict[num] = i
        return None


s = Solution()
nums = [2, 7, 11, 15]
target = 18
print(s.twoSum(nums, target))
