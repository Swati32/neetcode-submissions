
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque([root])
        result = []
        while queue:
            level = []
            for i in range(len(queue)):
                popped = queue.popleft()
                level.append(popped.val)

                if popped.left:
                    queue.append(popped.left)

                if popped.right:
                    queue.append(popped.right)
            result.append(level)

        return result

        