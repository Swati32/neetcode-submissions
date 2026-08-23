# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        queue = deque([root])
        while queue:
            popped = queue.popleft()
            temp = popped.right
            popped.right = popped.left
            popped.left = temp

            if popped.left:
                queue.append(popped.left)
            if popped.right:
                queue.append(popped.right)

        return root