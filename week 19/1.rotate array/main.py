from collections import deque


class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        nums.reverse()
        k = k % len(nums)
        nums[:k] = reversed(nums[0:k])
        nums[k:] = reversed(nums[k:])

    def rotate2(self, nums: list[int], k: int) -> None:
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]

    def rotate3(self, nums: list[int], k: int) -> None:
        d = deque(nums)
        d.rotate(k)
        nums[:] = list(d)


s = Solution()

nums = [1, 2, 3, 4, 5, 6, 7]
print("original array:\n", nums)
k = 10

nums1 = nums.copy()
print("\nmethod 1:")
s.rotate(nums1, k)
print(nums1)

nums2 = nums.copy()
print("\nmethod 2:")
s.rotate2(nums2, k)
print(nums2)

nums3 = nums.copy()
print("\nmethod 3:")
s.rotate3(nums3, k)
print(nums3)
