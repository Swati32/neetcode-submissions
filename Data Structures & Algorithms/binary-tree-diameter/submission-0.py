# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_d = 0
        def diameter(root):
            nonlocal max_d
            if root is None:
                return 0 
            d_left = diameter(root.left) 
            d_right = diameter(root.right)

            nonlocal max_d
            max_d = max(max_d, d_left + d_right)
            return max(d_left, d_right) + 1

        diameter(root)
        return max_d
        