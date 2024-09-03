class Solution:
    def addDigits(self, num: int) -> int:
        if num <= 9:
            return num
        r = num % 9
        if r == 0:
            return 9
        return r


s = Solution()
print(s.addDigits(49))
