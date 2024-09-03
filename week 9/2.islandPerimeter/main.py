class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        area = 0
        row, col = len(grid), len(grid[0])

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    area += 4

                    if i > 0 and grid[i - 1][j] == 1:
                        area -= 2

                    if j > 0 and grid[i][j - 1] == 1:
                        area -= 2

        return area


s = Solution()
grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
print(s.islandPerimeter(grid))

