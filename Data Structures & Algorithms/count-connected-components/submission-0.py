class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find_parent(self, node):
        while self.parent[node] != node:
            node = self.parent[node]
        return node

        
    def union(self, u, v):
        pu = self.find_parent(u)
        pv = self.find_parent(v)

        if pu == pv:
            return False
        
        if self.rank[pu] > self.rank[pv]:
            self.parent[pv] = pu
            self.rank[pu] += 1
        else: 
            self.parent[pu] = pv
            self.rank[pv] += 1

        return True


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        res = n

        for u, v in edges:
            if dsu.union(u,v):
                res -= 1

        return res        

        



        