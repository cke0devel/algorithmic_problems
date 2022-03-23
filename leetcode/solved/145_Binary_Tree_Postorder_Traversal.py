# difficulty: Easy
# Runtime: 33 ms, faster than 77.58% of Python3 online submissions for Binary Tree Postorder Traversal.
# Memory Usage: 13.8 MB, less than 67.82% of Python3 online submissions for Binary Tree Postorder Traversal.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]

