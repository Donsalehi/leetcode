class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        result = 0
        for char in s:
            result ^= ord(char)
        for char in t:
            result ^= ord(char)
        return chr(result)


solution = Solution()
s = "abcd"
t = "dabcb"
print(solution.findTheDifference(s, t))
