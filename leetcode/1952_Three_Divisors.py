# difficulty: Easy
# Wrong Answer
#   Input: 81
#   Output: true
#   Expected: false

class Solution:
    def isThree(self, n: int) -> bool:
        import math

        k = int(math.sqrt(n))

        return k*k == n

