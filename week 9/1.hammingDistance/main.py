class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')


s = Solution()
x, y = 1, 3
print(s.hammingDistance(x, y))
