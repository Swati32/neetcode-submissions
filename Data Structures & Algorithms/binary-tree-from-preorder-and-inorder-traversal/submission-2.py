# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        in_map = {}
        for i, val in enumerate(inorder):
            in_map[val] = i

        self.idx = 0
        def construct (left, right):
            if left > right:
                return None
            
            root = TreeNode(preorder[self.idx])
            self.idx += 1

            mid = in_map[root.val] 
            root.left = construct(left, mid-1)
            root.right = construct(mid+1, right)

            return root
        
        return construct(0, len(inorder)-1)
