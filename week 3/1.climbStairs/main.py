class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        ans = [0] * (n+1)
        ans[1] = 1
        ans[2] = 2
        for i in range(3, n+1):
            ans[i] = ans[i-1] + ans[i-2]
        return ans[n]


s = Solution()
print(s.climbStairs(5))
