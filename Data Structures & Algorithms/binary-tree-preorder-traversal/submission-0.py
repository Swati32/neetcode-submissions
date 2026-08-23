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
        output = []
        stack = [root]
    
        while stack:
            popped = stack.pop()
            output.append(popped.val)

            if popped.right is not None:
                stack.append(popped.right)
            if popped.left is not None:
                stack.append(popped.left)    

        return output