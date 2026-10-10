class Solution:
    def findTargetSumWays(self, nums: list[int], t: int) -> int:
        total = sum(nums)
        if total < abs(t) or (total + t) % 2 != 0:
            return 0
    
        target = (total + t) // 2
        n = len(nums)
    
        dp = [[0] * (target + 1) for _ in range(n + 1)]
        dp[0][0] = 1  

        for i in range(1, n + 1):
            num = nums[i - 1]
            for j in range(target + 1):
                dp[i][j] = dp[i - 1][j]  # Exclude current number
                if j >= num:
                    dp[i][j] += dp[i - 1][j - num]  # Include current number
                
        return dp[n][target]