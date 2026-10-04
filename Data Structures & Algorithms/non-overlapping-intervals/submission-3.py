class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort by end time and then start time
        intervals.sort(key = lambda x: (x[1], x[0]))
        non_overlap_intervals = [intervals[0]]

        removals = 0
        for current in intervals[1:]:
            last = non_overlap_intervals[-1]
            if current[0] < last[1]:
                last[1] = min(current[1], last[1])
                removals += 1
            else:
                non_overlap_intervals.append(current)
                

        return removals
        
