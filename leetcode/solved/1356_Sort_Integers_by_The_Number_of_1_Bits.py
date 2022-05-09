# difficulty: Easy
# Runtime: 80 ms, faster than 74.87% of Python3 online submissions for Sort Integers by The Number of 1 Bits.
# Memory Usage: 14.2 MB, less than 34.47% of Python3 online submissions for Sort Integers by The Number of 1 Bits.

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        l = sorted([(bin(n).count('1'), n) for n in arr])

        return [n for b,n in l]


