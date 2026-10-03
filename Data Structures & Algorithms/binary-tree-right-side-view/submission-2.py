# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        queue = deque([root])
        result = []

        while queue:
            result.append(queue[0].val)
            for i in range(len(queue)):
                popped = queue.popleft()
                if popped.right:
                    queue.append(popped.right)
                if popped.left:
                    queue.append(popped.left)
        
        return result
            
