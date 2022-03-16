# difficulty: Easy
# Runtime: 38 ms, faster than 67.47% of Python3 online submissions for Pascal's Triangle II.
# Memory Usage: 13.9 MB, less than 75.30% of Python3 online submissions for Pascal's Triangle II.

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle = [[1]]

        for r in range(1, rowIndex+1):
            row = [1]
            for c in range(1, r):
                row.append(triangle[r-1][c-1] + triangle[r-1][c])
            row.append(1)

            triangle.append(row)

        return triangle[rowIndex]

