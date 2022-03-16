# difficulty: Easy
#Runtime: 40 ms, faster than 99.98% of Python3 online submissions for Richest Customer Wealth.
# Memory Usage: 13.9 MB, less than 39.76% of Python3 online submissions for Richest Customer Wealth.

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max([sum(account) for account in accounts])

