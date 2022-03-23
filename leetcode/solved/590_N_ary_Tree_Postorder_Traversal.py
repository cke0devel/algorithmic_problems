# difficulty: Easy
# Runtime: 44 ms, faster than 98.76% of Python3 online submissions for N-ary Tree Postorder Traversal.
# Memory Usage: 16.4 MB, less than 19.30% of Python3 online submissions for N-ary Tree Postorder Traversal.

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []

        res = []
        for child in root.children:
            res += self.postorder(child)
        res += [root.val]

        return res

