# difficulty: Easy
# Runtime: 24 ms, faster than 99.23% of Python3 online submissions for Average Salary Excluding the Minimum and Maximum Salary.
# Memory Usage: 13.9 MB, less than 60.43% of Python3 online submissions for Average Salary Excluding the Minimum and Maximum Salary.

class Solution:
    def average(self, salary: List[int]) -> float:
        salary = sorted(salary)[1:-1]

        return sum(salary) / len(salary)
