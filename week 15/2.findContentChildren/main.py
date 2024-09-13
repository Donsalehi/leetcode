class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()
        cookie = 0
        child = 0

        while cookie < len(s) and child < len(g):
            if s[cookie] >= g[child]:
                child += 1

            cookie += 1

        return child


solution = Solution()
g = [1, 2, 3]
s = [1, 1]
print(solution.findContentChildren(g, s))
