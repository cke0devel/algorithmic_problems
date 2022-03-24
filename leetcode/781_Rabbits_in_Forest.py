# difficulty: Medium
# Wrong Answer
#   Input: [[0,0,1,1,1]]
#   Output: 4
#   Expected: 6

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        return sum(n+1 for n in set(answers) if n>0) + answers.count(0)

