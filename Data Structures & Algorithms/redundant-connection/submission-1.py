class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        nodes = set()
        for u,v in edges:
            nodes.add(u)
            nodes.add(v)

        n = len(nodes)

        parent = [i for i in range(n+1)]
        rank = [0] * (n+1)

        def find_parent(node):
            if parent[node] != node:
                parent[node] = find_parent(parent[node])
            return parent[node]
        
        def union(u, v):
            pu = find_parent(u)
            pv = find_parent(v)

            if pu == pv:
                return False
            
            if rank[pu] > rank[pv]:
                parent[pv] = pu
            elif rank[pu] < rank[pv]:
                parent[pu] = pv
            else:
                parent[pv] = pu
                rank[pv] +=1

            return True
        
        for u,v in edges:
            if not union(u,v):
                return [u,v]
            



   