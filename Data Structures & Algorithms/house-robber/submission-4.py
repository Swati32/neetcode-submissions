class Solution:
    def rob(self, nums: List[int]) -> int:      
        dp = [0, 0]
        for i in range(len(nums)):
            temp = dp[1]
            dp[1] = max(dp[1], dp[0]+ nums[i])
            dp[0] = temp
            
        return dp[1]
        