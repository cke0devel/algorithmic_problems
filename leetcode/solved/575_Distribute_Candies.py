# difficulty: Easy
# Runtime: 852 ms, faster than 80.18% of Python3 online submissions for Distribute Candies.
# Memory Usage: 15.9 MB, less than 95.25% of Python3 online submissions for Distribute Candies.

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        from collections import Counter

        return min(len(Counter(candyType)), len(candyType) // 2)

