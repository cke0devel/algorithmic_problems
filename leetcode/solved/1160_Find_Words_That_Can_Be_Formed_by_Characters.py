# difficulty: Easy
# Runtime: 238 ms, faster than 52.51% of Python3 online submissions for Find Words That Can Be Formed by Characters.
# Memory Usage: 14.5 MB, less than 88.48% of Python3 online submissions for Find Words That Can Be Formed by Characters.

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        from collections import Counter

        base = Counter(chars)

        return sum([len(word) for word in words if Counter(word) <= base])


