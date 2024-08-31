class Solution:
    def reverse(self, x: int) -> int:
        reverse = 0
        if x < 0:
            sign = -1
            x = abs(x)
        else:
            sign = 1
        while x != 0:
            reverse = reverse * 10 + x % 10
            x //= 10
        if reverse < -2 ** 31 or reverse > 2 ** 31 - 1:
            return 0
        return reverse * sign


s = Solution()
print(s.reverse(-123))
