# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maximum = [0]
        def height(root):
            if not root:
                return 0
            left_max = height(root.left)
            right_max = height(root.right)

            maximum[0] = max(maximum[0], left_max+right_max)

            return max(left_max, right_max)+1
        
        height(root)
        return maximum[0]
