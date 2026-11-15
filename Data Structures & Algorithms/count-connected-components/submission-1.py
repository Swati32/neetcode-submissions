
        
class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        rank = [0] * n
        parent = [0] * n
        for i in range(n):
            parent[i] = i
        
        def find_parent(node):
            if parent[node] != node:
                parent[node] = find_parent(parent[node])
            return parent[node]
        
        def union(u,v):
            pu = find_parent(u)
            pv = find_parent(v)

            if pu == pv:
                return False
            
            if rank[pu] > rank[pv]:
                parent[pv] = pu
            elif rank[pu] > rank[pv]:
                parent[pu] = pv
            else:
                parent[pu] = pv
                rank[pv] +=1

            return True

        for u,v in edges:
            if union(u, v):
                n -= 1
        
        return n

