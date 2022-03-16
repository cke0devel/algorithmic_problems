# difficulty: Easy
# Runtime: 95 ms, faster than 5.46% of Python3 online submissions for Minimum Cost to Move Chips to The Same Position.
# Memory Usage: 13.8 MB, less than 70.06% of Python3 online submissions for Minimum Cost to Move Chips to The Same Position.

class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        from collections import Counter, defaultdict

        costs = defaultdict(int)
        c = Counter(position)

        for target,_ in c.items():
            for p,n in c.items():
                costs[target] += (abs(target-p)%2) * n

        return min(costs.values())

