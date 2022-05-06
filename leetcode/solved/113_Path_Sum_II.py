# difficulty: Medium
# Runtime: 79 ms, faster than 21.80% of Python3 online submissions for Path Sum II.
# Memory Usage: 15.7 MB, less than 55.66% of Python3 online submissions for Path Sum II.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root: Optional[TreeNode], targetSum: int, ans: List[List[int]], cur: List[int]):
        if root == None:
            return

        targetSum -= root.val
        cur.append(root.val)

        if root.left == None and root.right==None:
            if targetSum == 0:
                ans.append(cur[:])
            else:
                cur.pop()
                return

        self.dfs(root.left, targetSum, ans, cur)
        self.dfs(root.right, targetSum, ans, cur)

        cur.pop()


    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []

        self.dfs(root, targetSum, ans, [])

        return ans

