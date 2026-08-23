class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1
            
        frequency = {}
        for key, value in seen.items():
            if value in frequency:
                frequency[value].append(key)
            else:
                frequency[value] = [key]
        
        result = []
        f_sorted = sorted(frequency, reverse = True)
        for i in f_sorted:
            result += frequency[i]
        
        return result[:k]

