# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None
        if p.val == root.val or q.val == root.val:
            return root
        
        lca_left = self.lowestCommonAncestor(root.left,p,q)
        lca_right = self.lowestCommonAncestor(root.right,p,q)

        if lca_left and lca_right:
            return root
        
        return lca_left if lca_left else lca_right
