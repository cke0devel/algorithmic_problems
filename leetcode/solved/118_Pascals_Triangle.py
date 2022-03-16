# difficulty: Easy
# Runtime: 32 ms, faster than 86.74% of Python3 online submissions for Pascal's Triangle.
# Memory Usage: 13.9 MB, less than 38.27% of Python3 online submissions for Pascal's Triangle.

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1]]

        for r in range(1, numRows):
            row = [1]
            for c in range(1, r):
                row.append(triangle[r-1][c-1] + triangle[r-1][c])
            row.append(1)

            triangle.append(row)

        return triangle

