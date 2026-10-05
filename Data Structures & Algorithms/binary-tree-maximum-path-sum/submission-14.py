class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = [-math.inf]

        def max_path_sum(root):
            if not root:
                return 0
            
            left_max = max(max_path_sum(root.left), 0)
            right_max = max(max_path_sum(root.right), 0)

            max_sum[0] = max(max_sum[0], left_max + right_max + root.val)

            return root.val + max(left_max, right_max)
        
        max_path_sum(root)
        return max_sum[0]