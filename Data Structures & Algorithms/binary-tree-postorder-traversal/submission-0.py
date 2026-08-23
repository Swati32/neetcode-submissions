# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None :
            return []

        stack = [root]
        output = []

        while stack:
            popped = stack.pop()
            output.append(popped.val)

            if popped.left:
                stack.append(popped.left)
            if popped.right:
                stack.append(popped.right)
            
        output.reverse()
        return output