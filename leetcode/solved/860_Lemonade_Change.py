# difficulty: Easy
# Runtime: 1207 ms, faster than 38.98% of Python3 online submissions for Lemonade Change.
# Memory Usage: 18 MB, less than 40.19% of Python3 online submissions for Lemonade Change.

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten = 0, 0

        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if five == 0:
                    return False
                five -= 1
                ten += 1
            elif bill == 20:
                change = 15
                if ten > 0:
                    ten -= 1
                    change = 5
                if 5*five < change:
                    return False
                five -= change//5

        return True

