# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            return 1 + max(height(root.left), height(root.right))

        if root is None:
            return True

        left_hieght =  height(root.left)
        right_hieght = height(root.right)
        
        if abs(left_hieght-right_hieght) > 1:
            return False
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)



        