# difficulty: Medium
# Runtime: 371 ms, faster than 79.28% of Python3 online submissions for All Elements in Two Binary Search Trees.
# Memory Usage: 22.9 MB, less than 48.68% of Python3 online submissions for All Elements in Two Binary Search Trees.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root: TreeNode, l: List[int]):
        if root == None:
            return

        l.append(root.val)

        self.dfs(root.left, l)
        self.dfs(root.right, l)

    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        l1, l2 = [], []

        self.dfs(root1, l1)
        self.dfs(root2, l2)

        return sorted(l1 + l2)

