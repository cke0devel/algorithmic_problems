# difficulty: Easy
# Runtime: 43 ms, faster than 49.68% of Python3 online submissions for Reformat Date.
# Memory Usage: 13.8 MB, less than 98.56% of Python3 online submissions for Reformat Date.

class Solution:
    def reformatDate(self, date: str) -> str:
        monthNames = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

        day, month, year = date.split()

        day = ''.join([c for c in day if c.isdigit()]).rjust(2, '0')
        month = str(monthNames.index(month)+1).rjust(2, '0')

        return "-".join([year, month, day])
