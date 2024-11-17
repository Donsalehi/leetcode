class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        xor = 0
        for num in nums:
            xor ^= num

        diff_bit = xor & -xor

        num1, num2 = 0, 0
        for num in nums:
            if num & diff_bit:
                num1 ^= num
            else:
                num2 ^= num

        return [num1, num2]


s = Solution()
nums = [1, 2, 1, 3, 2, 5]
print(s.singleNumber(nums))
