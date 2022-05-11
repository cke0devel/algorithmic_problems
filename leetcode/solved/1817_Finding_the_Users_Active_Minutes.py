# difficulty: Medium
# Runtime: 1300 ms, faster than 48.11% of Python3 online submissions for Finding the Users Active Minutes.
# Memory Usage: 24.8 MB, less than 46.52% of Python3 online submissions for Finding the Users Active Minutes.

class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        from collections import defaultdict

        uam = defaultdict(set)

        for user, time in logs:
            uam[user].add(time)

        ans = [0]*k
        for k,v in uam.items():
            ans[len(v)-1] += 1

        return ans


