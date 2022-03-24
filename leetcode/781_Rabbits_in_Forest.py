# difficulty: Medium
# Wrong Answer
#   Input: [1,0,1,0,0]
#   Output: 3
#   Expected: 5

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        return sum(n+1 for n in set(answers))

