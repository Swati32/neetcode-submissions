class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
       
        islands = 0 
        visited = set()
        m, n = len(grid), len(grid[0])

        def dfs(r, c):
            if not 0 <= r < m or not 0 <= c < n or (r,c) in visited or grid[r][c] == "0":
                return 

            visited.add((r, c))
            
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)


        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i,j) not in visited:
                    dfs(i, j)
                    islands += 1
        
        return islands

