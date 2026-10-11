# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        pre_left = self.preorderTraversal(root.left)
        pre_right = self.preorderTraversal(root.right)

        return [root.val] + pre_left + pre_right