# difficulty: Easy
# Runtime: 98 ms, faster than 12.68% of Python3 online submissions for N-ary Tree Preorder Traversal.
# Memory Usage: 16.3 MB, less than 47.13% of Python3 online submissions for N-ary Tree Preorder Traversal.

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []

        res = [root.val]
        for child in root.children:
            res += self.preorder(child)

        return res

