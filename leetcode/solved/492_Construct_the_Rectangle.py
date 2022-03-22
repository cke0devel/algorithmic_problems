# difficulty: Easy
# Runtime: 51 ms, faster than 56.82% of Python3 online submissions for Construct the Rectangle.
#Memory Usage: 13.9 MB, less than 63.47% of Python3 online submissions for Construct the Rectangle.

class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        import math

        w = max(l for l in range(1, int(math.sqrt(area)+1)) if area%l == 0)
        l = area // w

        return [l, w]


