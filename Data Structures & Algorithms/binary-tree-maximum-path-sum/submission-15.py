class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = [-math.inf]

        def maxSum(node):
            if not node:
                return 0
        
            # Drop negative contributions immediately
            left_max = max(maxSum(node.left), 0)
            right_max = max(maxSum(node.right), 0)
        
            # Update global max through this node as the apex/split
            max_sum[0] = max(max_sum[0], left_max + right_max + node.val)

            # Return only one extending branch upward to parent
            return node.val + max(left_max, right_max)
        
        maxSum(root)
        return max_sum[0]