class Solution:
    def rob(self, nums: List[int]) -> int:      
        if not nums:
            return 0
        prev1, prev2 = nums[0], 0
        for i in range(1, len(nums)):
            max_robbed = max(prev2 + nums[i], prev1)
            prev2 = prev1
            prev1 = max_robbed
        
        return prev1
        