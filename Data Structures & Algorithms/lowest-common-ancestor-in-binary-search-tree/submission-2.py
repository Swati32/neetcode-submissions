# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or not p or not q:
            return None

        if root.val == p.val or root.val == q.val:
            return root
        
        if p.val < root.val < q.val or q.val < root.val< p.val:
            return root
        
        if p.val < root.val and q.val <root.val:
            return self.lowestCommonAncestor(root.left, p, q)

        return  self.lowestCommonAncestor(root.right, p, q)   