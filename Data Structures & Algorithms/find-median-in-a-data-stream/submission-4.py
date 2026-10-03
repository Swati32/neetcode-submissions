class MedianFinder:

    def __init__(self):
        self.large = [] # min_heap
        self.small = [] # max_heap
      
    def addNum(self, num: int) -> None:
        if self.large and num >= self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -num)

        if len(self.large) - len(self.small) > 1:
            popped = heapq.heappop(self.large)
            heapq.heappush(self.small, -popped)
        elif len(self.small) - len(self.large) > 1:
            popped = heapq.heappop(self.small)
            heapq.heappush(self.large, -popped)

      

    def findMedian(self) -> float:
        if not self.large and not self.small:
            return 0
        if len(self.large) == len(self.small):
            return (self.large[0] + (-self.small[0])) / 2
        elif len(self.large) >= len(self.small):
            return self.large[0]
        else:
            return -self.small[0]
            
        

        
        