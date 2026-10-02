class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visited = set()
        total_cost = 0
        min_heap = [(0, 0)] #cost, point
        n = len(points)

        while min_heap and len(visited) < n:
            cost, p1 = heapq.heappop(min_heap)
            if p1 in visited:
                continue
            
            total_cost += cost
            visited.add(p1)

            for p2 in range(n):
                if p2 not in visited:
                    dist = abs(points[p1][0] - points[p2][0]) + abs(points[p1][1] - points[p2][1])
                    heapq.heappush(min_heap, (dist, p2))
            
        return total_cost

            
        

