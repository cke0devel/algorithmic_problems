# difficulty: Easy
# Runtime: 92 ms, faster than 24.59% of Python3 online submissions for Final Value of Variable After Performing Operations.
# Memory Usage: 13.9 MB, less than 36.47% of Python3 online submissions for Final Value of Variable After Performing Operations.

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        func = lambda x: 1 if '+' in x else -1
        return sum([func(op) for op in operations])

