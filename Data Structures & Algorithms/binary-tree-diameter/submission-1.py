# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        diameter = self.height(root.left) + self.height(root.right)
        return max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right), diameter)

    
    def height(self, root:Optional[TreeNode]) -> int:
        if root is None:
            return 0

        return max(self.height(root.left), self.height(root.right))+1