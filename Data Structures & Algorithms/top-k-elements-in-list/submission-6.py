class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for num in nums:
            seen[num] = seen.get(num, 0) + 1
    
        frequency = {}
        for key, value in seen.items():
            frequency[value] = frequency.get(value, [])
            frequency[value].append(key)
        
        res = []
        for f in range(len(nums), 0, -1):
            if f in frequency:
                res += (frequency[f])
            if len(res) >= k:
                break

        return res
        





