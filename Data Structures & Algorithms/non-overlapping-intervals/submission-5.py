class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort by end time and then start time
        intervals.sort(key = lambda x: (x[1], x[0]))
        prev_end = intervals[0][1]
        removals = 0

        for start, end in intervals[1:]:
            if start < prev_end:
                removals += 1
            else:
                prev_end = end
                
        return removals
        
