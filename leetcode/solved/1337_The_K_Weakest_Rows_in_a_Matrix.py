# difficulty: Easy
# Runtime: 139 ms, faster than 63.37% of Python3 online submissions for The K Weakest Rows in a Matrix.
# Memory Usage: 14.2 MB, less than 92.88% of Python3 online submissions for The K Weakest Rows in a Matrix.

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        count = sorted([(row.count(1),i) for i,row in enumerate(mat)])

        return [i for _,i in count][:k]
