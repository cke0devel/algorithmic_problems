# difficulty: Easy
# Runtime: 185 ms, faster than 27.39% of Python3 online submissions for Find Smallest Letter Greater Than Target.
# Memory Usage: 14.3 MB, less than 73.15% of Python3 online submissions for Find Smallest Letter Greater Than Target.

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        import bisect

        return letters[bisect.bisect_right(letters, target) % len(letters)]

