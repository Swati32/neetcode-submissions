class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        adj = defaultdict(list)

        for v1, v2  in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)        

        def dfs(node, parent):
            visited.add(node)

            for neighbor in adj[node]:
                if neighbor != parent:
                    if neighbor in visited or not dfs(neighbor, node):
                        return False
            return True

        no_cycle = dfs(0, -1)
        return no_cycle and len(visited) == n
