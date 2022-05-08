# difficulty: Easy
# Runtime: 90 ms, faster than 56.17% of Python3 online submissions for Transpose Matrix.
# Memory Usage: 14.8 MB, less than 57.97% of Python3 online submissions for Transpose Matrix.

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transpose = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                transpose[j][i] = matrix[i][j]

        return transpose
