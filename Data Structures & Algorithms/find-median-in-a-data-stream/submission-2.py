class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        if len(self.max_heap)== 0:
            heapq.heappush(self.max_heap, num)
            return

        if self.max_heap[0] <= num:
            heapq.heappush(self.max_heap, num)
        else:
            heapq.heappush(self.min_heap, -num)

        if len(self.min_heap) > len(self.max_heap) + 1:
            popped = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -popped)
        elif len(self.max_heap) > len(self.min_heap) + 1:
            popped = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, -popped)
        

    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            return (-self.min_heap[0] + self.max_heap[0]) / 2
        elif len(self.min_heap) > len(self.max_heap):
            return -self.min_heap[0]
        else:
            return self.max_heap[0]
        

        
        