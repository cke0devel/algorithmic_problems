# difficulty: Medium
# Wrong Answer:
#   Input: [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
#   Output: 34
#   Expected: 19

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict

class Solution:
    depthSum = defaultdict(int)
    maxDepth = -1

    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        self._dfs(0, root)

        return self.depthSum[self.maxDepth]

    def _dfs(self, depth: int, root: Optional[TreeNode]) -> None:
        if root:
            self.maxDepth = max(self.maxDepth, depth)
            self.depthSum[depth] += root.val

            self._dfs(depth+1, root.left)
            self._dfs(depth+1, root.right)


