# difficulty: Medium
# Runtime: 2375 ms, faster than 19.45% of Python3 online submissions for Find Original Array From Doubled Array.
# Memory Usage: 33 MB, less than 29.49% of Python3 online submissions for Find Original Array From Doubled Array.

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        from collections import defaultdict

        c = defaultdict(int)

        for n in sorted(changed):
            c[n] += 1

        ans = []
        if 0 in c:
            if c[0] % 2 == 1:
                return []
            ans += [0] * (c[0]//2)
            del c[0]

        for k in c.keys():
            if c[k] == 0:
                continue

            if k*2 not in c:
                return []

            if c[k] > c[k*2]:
                return []

            ans.extend([k] * c[k])
            c[k*2] -= c[k]
            c[k] = 0

        return ans
