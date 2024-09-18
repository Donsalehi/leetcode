class Solution:
    def canJump1(self, nums: list[int]) -> bool:
        max_reachable = 0
        wanted = len(nums) - 1

        for i, jump in enumerate(nums):
            if i > max_reachable:
                return False

            max_reachable = max(max_reachable, i + jump)

            if max_reachable >= wanted:
                return True

    def canJump2(self, nums: list[int]) -> bool:
        total = 0

        for num in nums:
            if total < 0:
                return False
            if num > total:
                total = num
            total -= 1

        return True


s = Solution()
nums1 = [2, 3, 1, 1, 4]
print('function 1 solution:', s.canJump1(nums1))
print('function 2 solution:', s.canJump2(nums1))
print('-------------------------------------------')
nums2 = [3, 2, 1, 0, 4]
print('function 1 solution:', s.canJump1(nums2))
print('function 1 solution:', s.canJump2(nums2))
