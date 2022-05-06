# difficulty: Easy
# Runtime: 90 ms, faster than 11.60% of Python3 online submissions for Three Consecutive Odds.
# Memory Usage: 13.9 MB, less than 58.52% of Python3 online submissions for Three Consecutive Odds.

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        cnt = 0

        for n in arr:
            if n%2 == 1:
                cnt += 1
                if cnt == 3:
                    return True
            else:
                cnt = 0

        return cnt == 3

