class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # A tree with n nodes must have exactly n - 1 edges
        if len(edges) != n - 1:
            return False
            
        visited = set()
        adj = defaultdict(list)
 
        for u, v  in edges:
            adj[u].append(v)
            adj[v].append(u)        

        def has_cycle(node, parent):
            visited.add(node)

            for neighbor in adj[node]:
                if neighbor != parent:
                    if neighbor in visited or has_cycle(neighbor, node):
                        return True
            return False

        no_cycle = not has_cycle(0, -1)
        return no_cycle and len(visited) == n
