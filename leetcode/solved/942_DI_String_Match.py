# difficulty: Easy
# Runtime: 63 ms, faster than 89.41% of Python3 online submissions for DI String Match.
# Memory Usage: 15.3 MB, less than 50.54% of Python3 online submissions for DI String Match.

class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        low, high = 0, len(s)

        ans = []
        for c in s:
            if c == 'I':
                ans.append(low)
                low += 1
            else:
                ans.append(high)
                high -= 1

        ans.append(low)
        return ans


