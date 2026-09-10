"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        
        intervals.sort(key=lambda x: x.start)
        active_rooms = []

        for interval in intervals:
            if active_rooms and active_rooms[0] <= interval.start:
                heapq.heappop(active_rooms)

            heapq.heappush(active_rooms, interval.end)
            
        return len(active_rooms)
