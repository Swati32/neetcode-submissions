class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-s for s in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
           first = -heapq.heappop(max_heap)
           second = -heapq.heappop(max_heap)

           remaining = first-second
           if remaining:
                heapq.heappush(max_heap, -remaining)
            
        return -max_heap[0] if max_heap else 0

        