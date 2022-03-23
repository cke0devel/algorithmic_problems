# difficulty: Medium
# Runtime: 56 ms, faster than 43.54% of Python3 online submissions for Reordered Power of 2.
# Memory Usage: 13.8 MB, less than 73.43% of Python3 online submissions for Reordered Power of 2.

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        from collections import Counter

        powerof2 = [Counter(str(2**i)) for i in range(64) if len(str(2**i)) <= 9]

        c = Counter(str(n))

        return any(c==e for e in powerof2)


