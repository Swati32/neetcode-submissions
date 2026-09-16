# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    
        in_map = {}
        for i, node in enumerate(inorder):
            in_map[node] = i

        
        def construct(p_start, p_end, i_start, i_end):
            if p_start > p_end or i_start > i_end:
                return None
                
            root_val = preorder[p_start]
            root = TreeNode(root_val)
            mid = in_map[root_val]

            len_left = mid - i_start


            root.left = construct(
                p_start + 1,
                p_start + len_left,
                i_start,
                mid
            )
            root.right = construct(
                p_start + len_left + 1,
                p_end,
                mid + 1,
                i_end
            )

            return root
        
        n = len(preorder)
        return construct(0, n-1, 0, n-1)
