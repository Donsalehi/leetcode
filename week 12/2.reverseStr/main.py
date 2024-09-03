class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        length = len(s)

        if k == 1 or length == 1:
            return s

        s_list = list(s)

        for i in range(0, length, 2 * k):
            s_list[i: i + k] = reversed(s_list[i: i + k])

        return ''.join(s_list)


solution = Solution()
s = "abcdefghij"
k = 2
print(solution.reverseStr(s, k))
