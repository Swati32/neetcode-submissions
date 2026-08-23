# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        def is_balanced(root):
            if root is None:
                return (True, 0)
            (left_balanced, left_hieght) = is_balanced(root.left)
            (right_balanced, right_hieght) = is_balanced(root.right)

            balanced = (left_balanced and right_balanced) and (abs(right_hieght-left_hieght) <= 1)
            return (balanced, max(left_hieght,right_hieght) +1 )

        (balanced, height) = is_balanced(root)
        return balanced
        