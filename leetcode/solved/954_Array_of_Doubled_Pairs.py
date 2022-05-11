# difficulty: Medium
# Runtime: 834 ms, faster than 53.60% of Python3 online submissions for Array of Doubled Pairs.
# Memory Usage: 16.6 MB, less than 63.18% of Python3 online submissions for Array of Doubled Pairs.

class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        from collections import OrderedDict

        arr = sorted(arr, key=lambda x: abs(x))
        freq = OrderedDict()

        for n in arr:
            if n not in freq:
                freq[n] = 1
            else:
                freq[n] += 1

        if 0 in freq:
            if freq[0] % 2 != 0:
                return False

            del freq[0]

        while freq:
            n = next(iter(freq))

            if n*2 not in freq:
                return False

            freq[n] -= 1
            freq[n*2] -= 1

            if freq[n] == 0:
                del freq[n]
            if freq[n*2] == 0:
                del freq[n*2]

        return True

