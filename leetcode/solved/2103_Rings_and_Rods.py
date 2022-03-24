# difficulty: Easy
# Runtime: 40 ms, faster than 60.59% of Python3 online submissions for Rings and Rods.
# Memory Usage: 14 MB, less than 22.53% of Python3 online submissions for Rings and Rods.

class Solution:
    def countPoints(self, rings: str) -> int:
        rods = [set() for _ in range(10)]

        for p in range(0, len(rings), 2):
            color, rod = rings[p:p+2]

            rods[int(rod)].add(color)

        return sum(len(rod)==3 for rod in rods)


