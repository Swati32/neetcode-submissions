class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        rotten = 0

        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1

        minutes = 0
        visited = set()
        while queue and fresh > 0:
            level = len(queue)
            for i in range(level):
                r,c = queue.popleft()
                directions = [(0,1), (0,-1), (1,0), (-1,0)]
                for dr, dc in directions:
                    nr, nc = dr + r, c + dc
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1 and (nr, nc) not in visited:
                        fresh -= 1
                        visited.add((nr,nc))
                        queue.append((nr,nc)) 

            minutes += 1
        return minutes if fresh == 0 else -1




        