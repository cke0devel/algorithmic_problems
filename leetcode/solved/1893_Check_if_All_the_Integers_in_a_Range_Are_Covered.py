# difficulty: Easy
# Runtime: 78 ms, faster than 18.65% of Python3 online submissions for Check if All the Integers in a Range Are Covered.
# Memory Usage: 13.9 MB, less than 82.54% of Python3 online submissions for Check if All the Integers in a Range Are Covered.

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for n in range(left, right+1):
            found = False

            for start, end in ranges:
                if start<=n and n<=end:
                    found = True
                    break

            if not found:
                return False

        return True
