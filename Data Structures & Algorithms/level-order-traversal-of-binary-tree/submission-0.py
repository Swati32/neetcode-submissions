# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        queue = deque([root])
        
        while queue:
            queue_length = len(queue)
            res.append([])
            for i in range(queue_length):
                popped = queue.popleft()
                res[-1].append(popped.val)

                if popped.left:
                    queue.append(popped.left)
                if popped.right:
                    queue.append(popped.right)    


        return res