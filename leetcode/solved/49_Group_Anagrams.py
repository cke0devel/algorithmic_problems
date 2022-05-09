# difficulty: Medium
# Runtime: 203 ms, faster than 14.51% of Python3 online submissions for Group Anagrams.
# Memory Usage: 17.8 MB, less than 65.84% of Python3 online submissions for Group Anagrams.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = sorted([(''.join(sorted(word)), word) for word in strs])

        ans = []
        prev = None

        for anagram, word in words:
            if prev==None or prev!=anagram:
                ans.append([])

            ans[-1].append(word)
            prev = anagram

        return ans

