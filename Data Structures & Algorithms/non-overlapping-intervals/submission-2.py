class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort by end time
        intervals.sort(key = lambda x: (x[1], x[0]))
        last_end_time = intervals[0][1]

        removals = 0
        for current in intervals[1:]:
            if current[0] < last_end_time:
                last_end_time = min(last_end_time, current[1])
                removals += 1
            else:
                last_end_time = current[1]

        return removals
        
