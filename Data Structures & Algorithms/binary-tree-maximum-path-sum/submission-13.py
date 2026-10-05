# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = [-math.inf]

        def maxSum(root):
            if not root:
                return 0
        
            left_max = maxSum(root.left)
            right_max = maxSum(root.right)
        
            max_val = max(left_max + root.val, right_max + root.val, root.val)

            max_sum[0] = max(max_val, max_sum[0], left_max + right_max + root.val)

            return max_val
        
        maxSum(root)
        return max_sum[0]





        
