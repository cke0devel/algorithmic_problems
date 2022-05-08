# difficulty: Easy
# Runtime: 58 ms, faster than 23.32% of Python3 online submissions for Build an Array With Stack Operations.
# Memory Usage: 14 MB, less than 18.33% of Python3 online submissions for Build an Array With Stack Operations.

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []

        targetIdx = 0
        for i in range(1, n+1):
            ans.append('Push')

            if target[targetIdx] != i:
                ans.append('Pop')
            else:
                targetIdx += 1

            if targetIdx >= len(target):
                break

        return ans


