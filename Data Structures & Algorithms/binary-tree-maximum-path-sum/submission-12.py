# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = [-math.inf]

        def dfs(root):
            if not root:
                return 0
            
            # 1. Prune negative paths right away
            left_sum = max(dfs(root.left), 0)
            right_sum = max(dfs(root.right), 0)

            # 2. Arch path through the current node as the peak
            max_sum[0] = max(max_sum[0], left_sum + right_sum + root.val)

            # 3. Extend only the single best downward path to the parent
            return max(left_sum, right_sum) + root.val

        dfs(root)
        return max_sum[0]



        
