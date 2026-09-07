class Solution:
    def rob(self, nums: List[int]) -> int:     
        if not nums:
            return 0 
        if len(nums) == 1:
            return nums[0]
        
        def helper(arr):
            dp = [0, arr[0]]
            i = 1
            while i < len(arr):
                temp = dp[1]
                dp[1] = max(dp[1], dp[0]+ arr[i])
                dp[0] = temp
                i += 1
            return dp[1]
        
        return max(helper(nums[:len(nums)-1]), helper(nums[1:]))