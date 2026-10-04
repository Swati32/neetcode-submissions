"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # Base case: agar koi meeting nahi hai toh 0 rooms
        if not intervals:
            return 0 

        
      # Kya sabse pehle free hone wala room current meeting ke start tak khali ho chuka hai?
        # Haan, room free ho gaya! Purane bande ko nikalo (room reuse ho gaya)

        # Taaki hum pehle shuru hone wali meetings ko pehle handle karein
        intervals.sort(key = lambda x: x.start)

        # min_heap[0] hamesha batayega sabse jaldi kaunsa room khali hone wala hai
        min_heap = []
        heapq.heappush(min_heap, intervals[0].end)

        for interval in intervals[1:]:
            #Kya sabse pehle free hone wala room current meeting ke start tak khali ho chuka hai
            if interval.start >= min_heap[0]:
                # Haan, room free ho gaya! Purane bande ko nikalo (room reuse ho gaya)
                heapq.heappop(min_heap)
            # Chahe purana room reuse hua ho ya naya room open kiya ho,
            # is meeting ka end time heap me daal do
            heapq.heappush(min_heap, interval.end)

        return len(min_heap)
