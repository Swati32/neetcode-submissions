# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if not node:
                return 0
            
            max_left = height(node.left)
            if max_left == -1:
                return -1

            max_right = height(node.right)
            if max_right == -1:
                return -1
            
            if abs(max_left-max_right) > 1:
                return -1
            
            return max(max_left, max_right) + 1
        
        return False if height(root) < 0 else True
            