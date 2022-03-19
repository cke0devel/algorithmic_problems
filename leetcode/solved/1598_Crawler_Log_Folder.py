# difficulty: Easy
# Runtime: 48 ms, faster than 88.79% of Python3 online submissions for Crawler Log Folder.
# Memory Usage: 14.2 MB, less than 53.30% of Python3 online submissions for Crawler Log Folder.

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0

        for log in logs:
            if log == "../":
                depth = max(0, depth-1)
            elif log != "./":
                depth += 1

        return depth

