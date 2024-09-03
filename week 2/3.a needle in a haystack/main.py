class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1


s = Solution()
haystack = "Hello, how are you?"
needle = "how"
print(s.strStr(haystack, needle))
