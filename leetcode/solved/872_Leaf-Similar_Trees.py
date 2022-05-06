# difficulty: Easy
# Runtime: 48 ms, faster than 41.41% of Python3 online submissions for Leaf-Similar Trees.
# Memory Usage: 13.8 MB, less than 88.14% of Python3 online submissions for Leaf-Similar Trees.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root: Optional[TreeNode], leaves: List[int]):
        if root == None:
            return

        self.dfs(root.left, leaves)
        self.dfs(root.right, leaves)

        if root.left==None and root.right==None:
            leaves.append(root.val)


    def getLeaves(self, root: Optional[TreeNode]) -> List[int]:
        leaves = []

        self.dfs(root, leaves)

        return leaves

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        return self.getLeaves(root1) == self.getLeaves(root2)

