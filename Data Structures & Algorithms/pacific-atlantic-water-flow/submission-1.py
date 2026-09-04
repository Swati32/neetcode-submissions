class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [(0,1), (0, -1), (1,0), (-1,0)]
        pac = [[False] * COLS for _ in range(ROWS)]
        atl = [[False] * COLS for _ in range(ROWS)]

        def bfs(source, ocean):
            queue = deque(source)
            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if nr >= 0 and nc >= 0 and nr <ROWS and nc <COLS and heights[nr][nc] >= heights[r][c] and not ocean[nr][nc]:
                        ocean[nr][nc] = True
                        queue.append((nr,nc))
            
        pacific = []
        atlantic = []
        for i in range(ROWS):
            pac[i][0] = True
            pacific.append((i,0))

            atl[i][COLS-1] = True
            atlantic.append((i, COLS-1))

        for i in range(COLS):
            pac[0][i] = True
            pacific.append((0,i))

            atl[ROWS-1][i] = True
            atlantic.append((ROWS-1, i))
        
        bfs(pacific, pac)
        bfs(atlantic, atl)

        res = []
        for i in range(ROWS):
            for j in range(COLS):
                if pac[i][j] and atl[i][j]:
                    res.append((i,j))
        return res
                        

