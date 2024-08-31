class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        strs.sort()
        ans = ""

        first = strs[0]
        last = strs[-1]
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return ans
            else:
                ans += first[i]
        return ans


s = Solution()
strs = ["flower", "flow", "flight"]
print(s.longestCommonPrefix(strs))
