# Difficulty: Medium
# Runtime: 43 ms, faster than 63.29% of Python3 online submissions for Simplify Path.
# Memory Usage: 14 MB, less than 57.22% of Python3 online submissions for Simplify Path.

class Solution:
    def simplifyPath(self, path: str) -> str:
        tokens = []
        for token in path.split("/"):
            if token in ["", "."]:
                continue
            if token == "..":
                if tokens:
                    tokens.pop()
                continue

            tokens.append(token)

        path = "/" + "/".join(tokens)

        return path
