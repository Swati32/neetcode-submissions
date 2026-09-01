
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = deque([root])
        result = []
        while queue:
            qlen = len(queue)
            level = []
            for j in range(qlen):
                popped = queue.popleft()
                level.append(popped.val)
                if popped.left:
                    queue.append(popped.left)
                if popped.right:
                    queue.append(popped.right)
            result.append(level)
            
        return result
    
            

        