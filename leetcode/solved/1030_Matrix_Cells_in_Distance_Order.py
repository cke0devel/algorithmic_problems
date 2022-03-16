# difficulty: Easy
# Runtime: 214 ms, faster than 61.49% of Python3 online submissions for Matrix Cells in Distance Order.
# Memory Usage: 16.7 MB, less than 23.58% of Python3 online submissions for Matrix Cells in Distance Order.

class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        distanceList = []

        for r in range(rows):
            for c in range(cols):
                distanceList.append((abs(r-rCenter)+abs(c-cCenter), r, c))

        return [[r,c] for d,r,c in sorted(distanceList)]


