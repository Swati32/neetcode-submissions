class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            res = target - nums[i]
            if res in seen:
                return [seen[res], i]
            else:
                seen[nums[i]] = i
        
        return [-1, -1]