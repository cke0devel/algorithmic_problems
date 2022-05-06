# difficulty: Medium
# Runtime: 69 ms, faster than 5.15% of Python3 online submissions for Sum Root to Leaf Numbers.
# Memory Usage: 13.8 MB, less than 68.57% of Python3 online submissions for Sum Root to Leaf Numbers.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root:Optional[TreeNode], s:int) -> int:
        if root == None:
            return 0

        s = s*10 + root.val

        if root.left == None and root.right == None:
            return s

        return self.dfs(root.left, s) + self.dfs(root.right, s)

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 0)


