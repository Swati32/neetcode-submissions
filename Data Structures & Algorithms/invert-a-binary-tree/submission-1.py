# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: 
            return root
        
        queue = deque([root])

        while queue:
            popped = queue.pop()
            temp = popped.left
            popped.left = popped.right
            popped.right = temp

            if popped.left:
                queue.append(popped.left)
            if popped.right:
                queue.append(popped.right)
        
        return root