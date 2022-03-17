# difficulty: Medium
# Runtime: 254 ms, faster than 60.32% of Python3 online submissions for Simplified Fractions.
# Memory Usage: 14.4 MB, less than 91.80% of Python3 online submissions for Simplified Fractions.

class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        import math

        ans = []

        for deno in range(2, n+1):
            for numer in range(1, deno):
                if math.gcd(numer, deno) == 1:
                    ans.append(f"{numer}/{deno}")

        return ans

