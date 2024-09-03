class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = bin(n)
        return binary.count('1')


s = Solution()
print(s.hammingWeight(2147483645))
