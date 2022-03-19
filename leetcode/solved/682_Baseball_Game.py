# difficulty: Easy
# Runtime: 40 ms, faster than 91.85% of Python3 online submissions for Baseball Game.
# Memory Usage: 14.1 MB, less than 50.63% of Python3 online submissions for Baseball Game.

class Solution:
    def calPoints(self, ops: List[str]) -> int:
        record = []

        for op in ops:
            if op == '+':
                record.append(record[-1] + record[-2])
            elif op == 'D':
                record.append(record[-1] * 2)
            elif op == 'C':
                record.pop()
            else:
                record.append(int(op))

        return sum(record)

