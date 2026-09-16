class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return n
        dp = [1,2]
        for i in range(3, n+1):
            temp = dp[0] + dp[1]
            dp[0] = dp[1]
            dp[1] = temp

        return dp[1]