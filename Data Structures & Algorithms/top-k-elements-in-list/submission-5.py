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
        for i in range(len(nums), 0, -1):
            if i in frequency:
                result += frequency[i]
        
        return result[:k]

