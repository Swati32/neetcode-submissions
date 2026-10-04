# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def height(root) -> int:
            if not root:
                return 0

            left_height = height(root.left)
            if left_height == -1:
                return -1
            
            right_height = height(root.right)
            if right_height == -1:
                return -1
            
            if abs(left_height - right_height) > 1:
                return -1

            return max(left_height, right_height) + 1

        return height(root) != -1