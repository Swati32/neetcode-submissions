# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        max_path_sum = [-math.inf]

        def dfs(node):
            if not node:
                return 0

            left_sum = max(dfs(node.left), 0)
            right_sum = max(dfs(node.right), 0)

            max_path_sum[0] = max(max_path_sum[0], left_sum + right_sum + node.val)
            return max(left_sum, right_sum) + node.val

        dfs(root)
        return max_path_sum[0]

