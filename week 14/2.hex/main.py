class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return str(num)

        if num < 0:
            num += 2 ** 32

        hex_chars = '0123456789abcdef'
        result = ''

        while num > 0:
            result += hex_chars[num & 15]
            num >>= 4

        return result[::-1]


s = Solution()
num1 = 26
print(s.toHex(num1))
num2 = -1
print(s.toHex(num2))
