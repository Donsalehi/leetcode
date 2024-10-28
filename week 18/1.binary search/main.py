class Solution:
    def search(self, nums: list[int], target: int) -> int:
        first = 0
        end = len(nums) - 1

        while first <= end:
            mid = (first + end) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                first = mid + 1
            else:
                end = mid - 1

        return -1


s = Solution()
nums = [-1, 0, 3, 5, 9, 12]
target = 9
print(s.search(nums, target))
