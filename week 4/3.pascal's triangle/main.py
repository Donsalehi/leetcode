class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        triangle = []
        for i in range(numRows):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = triangle[i-1][j-1] + triangle[i-1][j]
            triangle.append(row)
        return triangle

    def generate2(self, numRows: int) -> list[list[int]]:
        if numRows == 1:
            return [[1]]

        prev = self.generate2(numRows - 1)
        row = [1] * numRows

        for i in range(1, numRows - 1):
            row[i] = prev[-1][i - 1] + prev[-1][i]

        prev.append(row)

        return prev


s = Solution()
print(s.generate(6))
print(s.generate2(6))
