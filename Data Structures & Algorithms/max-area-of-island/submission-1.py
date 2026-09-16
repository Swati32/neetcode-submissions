class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()

        def dfs(r:int, c:int) -> area:
            if not 0 <= r <len(grid) or not 0 <= c < len(grid[0]):
                return 0
            if (r,c) in visited or grid[r][c] == 0:
                return 0

            visited.add((r,c))
            
            area = 1
            neighbors = [(0,1), (0,-1), (1,0), (-1,0)]
            for nr, nc in neighbors:
                area += dfs(r+nr, c+nc)
            
            return area


        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i,j) not in visited:
                    max_area = max(max_area, dfs(i, j))

        return max_area