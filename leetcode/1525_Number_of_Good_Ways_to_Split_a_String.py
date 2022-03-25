# difficulty: Medium
# Wrong Answer
#   Input: "aaaaa"
#   Output: 5
#   Expected: 4

class Solution:
    def numSplits(self, s: str) -> int:
        from collections import Counter

        left, right = Counter(""), Counter(s)

        ans = 0
        for c in s:
            left[c] += 1
            right[c] -= 1

            if len(set(left.keys())) == len(set(right.keys())):
                ans += 1

        return ans

