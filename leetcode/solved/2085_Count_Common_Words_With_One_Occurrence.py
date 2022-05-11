# difficulty: Easy
# Runtime: 102 ms, faster than 60.07% of Python3 online submissions for Count Common Words With One Occurrence.
# Memory Usage: 14.5 MB, less than 9.32% of Python3 online submissions for Count Common Words With One Occurrence.

class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        from collections import Counter

        c1 = Counter(words1)
        c2 = Counter(words2)

        ans = 0
        for k,v in c1.items():
            if v==1 and k in c2 and c2[k]==1:
                ans += 1

        return ans

