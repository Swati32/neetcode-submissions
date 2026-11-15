from collections import deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n
      
        for node in range(n):
            if color[node] != -1:
                continue

            color[node] = 0
            queue = deque([node])

            while queue:
                popped = queue.popleft()
                for neighbor in graph[popped]:
                    if color[neighbor] == -1:
                        color[neighbor] = 1-color[popped]
                        queue.append(neighbor)
                    elif color[neighbor] == color[popped]:
                        return False
            
        return True
