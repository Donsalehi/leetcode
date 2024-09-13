class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        closest_sum = float('inf')
        n = len(nums)

        for i in range(n - 2):
            left, right = i + 1, n - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum

                if current_sum < target:
                    left += 1

                elif current_sum > target:
                    right -= 1

                else:
                    return current_sum

        return closest_sum


s = Solution()
nums = [-1, 2, 1, -4]
target = 1
print(s.threeSumClosest(nums, target))
