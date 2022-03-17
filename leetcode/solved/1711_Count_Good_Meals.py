# difficulty: Medium
# Runtime: 1432 ms, faster than 64.88% of Python3 online submissions for Count Good Meals.
# Memory Usage: 21.7 MB, less than 51.79% of Python3 online submissions for Count Good Meals.

class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        from collections import Counter

        power2 = [2**i for i in range(22)]

        deliciousness.sort()
        c = Counter(deliciousness)

        ans = 0

        for i,v in enumerate(deliciousness):
            c[v] -= 1

            for p in power2:
                target = p-v

                if target in c:
                    ans += c[target]

        return ans % (10**9 + 7)

