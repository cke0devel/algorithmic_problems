# Difficulty: Easy
# Runtime: 119 ms, faster than 58.78% of Python3 online submissions for Counting Bits.
# Memory Usage: 20.8 MB, less than 37.20% of Python3 online submissions for Counting Bits.

class Solution:
    def countBits(self, n: int) -> List[int]:
        return [f"{num:b}".count("1") for num in range(n+1)]
