# difficulty: Medium
# Wrong Answer

class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        from collections import Counter

        power2 = [2**i for i in range(20) if 2**i<2*10**5]

        deliciousness.sort()
        c = Counter(deliciousness)

        ans = 0

        for i,v in enumerate(deliciousness):
            c[v] -= 1

            for p in power2:
                target = p-v

                if target in c:
                    ans += c[target]

        return ans

