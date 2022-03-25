# difficulty: Easy
# Runtime: 42 ms, faster than 60.01% of Python3 online submissions for Valid Parentheses.
# Memory Usage: 14 MB, less than 31.78% of Python3 online submissions for Valid Parentheses.

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c in "([{":
                stack.append(c)
            elif c == ")":
                if not stack or stack.pop() != "(":
                    return False
            elif c == "]":
                if not stack or stack.pop() != "[":
                    return False
            elif c == "}":
                if not stack or stack.pop() != "{":
                    return False

        return len(stack) == 0

