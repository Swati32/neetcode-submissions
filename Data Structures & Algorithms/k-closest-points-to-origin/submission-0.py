class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x,y in points:
            distance = math.sqrt(x**2 + y**2)
            heapq.heappush(heap, (distance, x, y))
        
        res = []
        for i in range(k):
            dist, x, y = heapq.heappop(heap)
            res.append([x,y])
        
        return res



