class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curr_sum = 0
        
        for num in nums:
            curr_sum += num
            max_sum = max(max_sum, curr_sum)
            
            # If our running sum drops below zero, it's a dead weight—drop it!
            if curr_sum < 0:
                curr_sum = 0
                
        return max_sum








        
