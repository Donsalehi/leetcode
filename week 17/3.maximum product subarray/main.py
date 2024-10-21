class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        max_so_far = min_so_far = result = nums[0]

        for i in range(1, len(nums)):
            current_max = max_so_far

            max_so_far = max(nums[i], nums[i] * max_so_far, nums[i] * min_so_far)
            min_so_far = min(nums[i], nums[i] * current_max, nums[i] * min_so_far)

            result = max(max_so_far, result)

        return result


s = Solution()
nums = [2, 3, -2, 4]
print(s.maxProduct(nums))
