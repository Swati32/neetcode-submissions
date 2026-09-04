"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        cloned_nodes = {}
        def clone(node):
            new_node = Node(node.val)
            cloned_nodes[node.val] = new_node

            for neighbor in node.neighbors:
                if neighbor.val in cloned_nodes:
                    new_node.neighbors.append(cloned_nodes[neighbor.val])
                else:
                    new_node.neighbors.append(clone(neighbor))
            
            return new_node

        return clone(node)



