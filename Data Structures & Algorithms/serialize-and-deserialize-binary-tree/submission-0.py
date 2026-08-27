# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "N"
        queue = deque([root]) 
        res = []
        while queue:
            popped = queue.popleft()
            if not popped:
                res.append("N")
            else:
                res.append(str(popped.val))
                queue.append(popped.left)
                queue.append(popped.right)  
        return ",".join(res)
            

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        if vals[0] == "N":
            return None
        root = TreeNode(int(vals[0]))
        queue = deque([root])
        index = 1
        while queue:
            popped = queue.popleft()
            if vals[index] != "N":
                popped.left = TreeNode(int(vals[index]))
                queue.append(popped.left)
            index+= 1
            if vals[index] != "N":
                popped.right = TreeNode(int(vals[index]))
                queue.append(popped.right)
            index+= 1
        return root
