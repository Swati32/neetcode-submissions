class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key = lambda x: x[0])

        result = [intervals[0]]

        for current in intervals:
            last_merged = result[-1]

            if last_merged[1] >= current[0]:
                last_merged[1] = max(last_merged[1], current[1])
            else:
                result.append(current)

        return result    
            
        