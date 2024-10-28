class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        return list(set(nums1).intersection(set(nums2)))


s = Solution()
nums1 = [4, 4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
print(s.intersection(nums1, nums2))
