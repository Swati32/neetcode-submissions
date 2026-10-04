# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = [0]

        def dfs(root):
            if not root:
                return 0
    
            d_left =  dfs(root.left)
            d_right = dfs(root.right)

            diameter[0] = max(d_left + d_right, diameter[0]) 
            return max(d_left, d_right) + 1
        
        dfs(root)
        return diameter[0]