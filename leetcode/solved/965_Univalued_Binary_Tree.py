# difficulty: Easy
# Runtime: 55 ms, faster than 25.28% of Python3 online submissions for Univalued Binary Tree.
# Memory Usage: 13.9 MB, less than 74.40% of Python3 online submissions for Univalued Binary Tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        left = (not root.left) or (self.isUnivalTree(root.left) and root.val == root.left.val)
        right = (not root.right) or (self.isUnivalTree(root.right) and root.val == root.right.val)

        return (left and right)

