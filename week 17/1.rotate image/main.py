class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(n):
            matrix[i].reverse()

    def rotate2(self, matrix: list[list[int]]):
        l, r = 0, len(matrix) - 1

        while l < r:
            for i in range(r - l):
                t, b = l, r

                temp = matrix[t][l + i]
                matrix[t][l + i] = matrix[b - i][l]
                matrix[b - i][l] = matrix[b][r - i]
                matrix[b][r - i] = matrix[t + i][r]
                matrix[t + i][r] = temp

            l += 1
            r -= 1


s = Solution()

print('first matrix')
matrix1 = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
print(matrix1)
s.rotate(matrix1)
print(matrix1)
print('------------------------------------------------------------------')
print('second matrix')
matrix2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix2)
s.rotate2(matrix2)
print(matrix2)
