class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        if grid[0][0] == 1 or grid[m-1][n-1] == 1:
            return -1
        if m == 1 and n == 1:
            return 1

        queue = deque([(0, 0,1)])
        directions = [(1,1), (1, -1), (-1, 1), (-1, -1), (0,-1), (1,0), (-1, 0), (0,1)]

        visited = set([(0,0)])
        while queue:
            r,c, length = queue.popleft()
            for dr, dc in directions:
                nr, nc = r+dr, c+dc 
                if 0<= nr < m and 0<= nc <n and grid[nr][nc] == 0 and (nr, nc) not in visited:
                    if nr == m - 1 and nc == n - 1:
                        return length+1
                    visited.add((nr, nc))
                    queue.append((nr, nc, length+1))
            
        return -1





        