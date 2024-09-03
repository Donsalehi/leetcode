class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        limit = len(candyType) // 2
        variety = len(set(candyType))
        return min(limit, variety)


s = Solution()
candyType = [1, 1, 2, 3, 4, 4]
print(s.distributeCandies(candyType))
