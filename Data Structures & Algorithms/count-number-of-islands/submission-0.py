class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visited = set()

        def is_island(r, c):
            if r < 0 or c <0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == "0" or (r,c) in visited:
                return
            
            visited.add((r,c))

            is_island(r+1, c) 
            is_island(r-1, c)
            is_island(r, c+1)
            is_island(r, c-1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i,j) not in visited:
                    is_island(i, j)
                    islands += 1
        
        return islands