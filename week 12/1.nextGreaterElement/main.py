class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        next_greater = {}
        stack = []

        for num in nums2:
            while stack and stack[-1] < num:
                next_greater[stack.pop()] = num
            stack.append(num)

        result = []
        for num in nums1:
            result.append(next_greater.get(num, -1))

        return result


s = Solution()
nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
print(s.nextGreaterElement(nums1, nums2))
