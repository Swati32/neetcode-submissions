class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n + 1))
        rank = [1] * (n + 1)

        def find(node: int) -> int:
            if node != parent[node]:
                parent[node] = find(parent[node])  # Path compression
            return parent[node]

        def union(u: int, v: int) -> bool:
            root_u, root_v = find(u), find(v)
            if root_u == root_v:
                return False
            
            if rank[root_u] < rank[root_v]:
                parent[root_u] = root_v
            elif rank[root_u] > rank[root_v]:
                parent[root_v] = root_u
            else:
                parent[root_u] = root_v
                rank[root_v] += 1
        
            return True
        
        for u, v in edges:
            if not union(u, v):
                return [u, v]

        return []
        