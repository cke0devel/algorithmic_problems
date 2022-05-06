# difficult: Medium
# Runtime: 46 ms, faster than 92.10% of Python3 online submissions for Smallest String Starting From Leaf.
# Memory Usage: 15.4 MB, less than 71.32% of Python3 online submissions for Smallest String Starting From Leaf.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root: Optional[TreeNode], path:str):
        if root == None:
            return path

        path = chr(ord('a') + root.val) + path

        if root.left == None and root.right == None:
            return path

        if root.left == None:
            return self.dfs(root.right, path)

        if root.right == None:
            return self.dfs(root.left, path)

        left = self.dfs(root.left, path)
        right = self.dfs(root.right, path)

        return min(left, right)


    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        return self.dfs(root, '')


