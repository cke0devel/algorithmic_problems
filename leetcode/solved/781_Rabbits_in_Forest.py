# difficulty: Medium
# Runtime: 58 ms, faster than 57.10% of Python3 online submissions for Rabbits in Forest.
# Memory Usage: 13.9 MB, less than 98.74% of Python3 online submissions for Rabbits in Forest.

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        from collections import Counter

        c = Counter(answers)

        ans = 0
        for k,v in c.items():
            if k == 0:
                ans += v
            else:
                ans += (k+1) * ((v+k) // (k+1))

        return ans

