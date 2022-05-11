# difficulty: Easy
# Runtime: 89 ms, faster than 42.23% of Python3 online submissions for Mean of Array After Removing Some Elements.
# Memory Usage: 14 MB, less than 38.27% of Python3 online submissions for Mean of Array After Removing Some Elements.

class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()

        p = len(arr) // 20
        return mean(arr[p:-p])

