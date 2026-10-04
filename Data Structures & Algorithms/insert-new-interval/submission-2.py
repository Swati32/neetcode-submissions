class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key = lambda x: x[0])

        result = [intervals[0]]
        for interval in intervals[1:]:
            if result[-1][1] >= interval[0]:
                result[-1][1] = max(interval[1], result[-1][1])
            else:
                result.append(interval)
            
        return result    
            
        