class Solution:
    def islandsAndTreasure(self, grid: list[list[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        INF = 2147483647
        queue = deque()

        # Step 1: Add all treasure chests to the queue as starting points
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))

        # Step 2: Multi-source BFS outward
        while queue:
            r, c = queue.popleft()

            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc

                # Only step into unvisited land cells (value is INF)
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == INF:
                    grid[nr][nc] = grid[r][c] + 1
                    queue.append((nr, nc))