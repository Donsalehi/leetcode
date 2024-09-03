class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n >= 1 and n & n-1 == 0


s = Solution()
print(s.isPowerOfTwo(32))
