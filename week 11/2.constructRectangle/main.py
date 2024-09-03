class Solution:
    def constructRectangle(self, area: int) -> list[int]:
        W = int(area ** 0.5)
        while area % W != 0:
            W -= 1
        L = area // W
        return [L, W]


s = Solution()
area = 122122
print(s.constructRectangle(area))
