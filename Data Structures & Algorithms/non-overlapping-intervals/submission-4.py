class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort by end time and then start time
        intervals.sort(key = lambda x: (x[1], x[0]))
        result = [intervals[0]]

        removals = 0
        for current in intervals[1:]:
            last = result[-1]
            if current[0] < last[1]:
                removals += 1
            else:
                result.append(current)
                

        return removals
        
