# difficulty: Easy
# Runtime: 131 ms, faster than 30.60% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
# Memory Usage: 15.6 MB, less than 83.85% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None

        if len(nums) == 1:
            return TreeNode(nums[0])

        mid = len(nums)//2

        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])

        return root

