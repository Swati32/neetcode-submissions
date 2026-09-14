class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            res = target - num
            if res in seen:
                return [seen[res], i]
            seen[num] = i
        
        return [-1, -1]