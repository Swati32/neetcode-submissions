class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        seen = Counter(nums)
        frequency = {}
        for key, value in seen.items():
            frequency[value] = frequency.get(value, [])
            frequency[value].append(key)
        
        res = []
        for f in range(len(nums), 0, -1):
            if f in frequency:
                res += frequency[f]
            if len(res) >= k:
                break

        return res
        '''
        f_map = Counter(nums)
        min_heap = []
      
        for num, freq in f_map.items():
            heapq.heappush(min_heap, (freq, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        result = []
        for freq, num in min_heap:
            result.append(num)
        return result





