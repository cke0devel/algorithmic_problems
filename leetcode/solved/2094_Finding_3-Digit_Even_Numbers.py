# difficulty: Easy
# Runtime: 6200 ms, faster than 12.38% of Python3 online submissions for Finding 3-Digit Even Numbers.
# Memory Usage: 13.9 MB, less than 65.41% of Python3 online submissions for Finding 3-Digit Even Numbers.

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        import itertools

        l = list(set(l for l in itertools.permutations(digits, 3) if l[0]!=0 and l[-1]%2==0))

        return sorted([n[0]*100 + n[1]*10 + n[2] for n in l])


