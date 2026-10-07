class Solution:
    def numSquares(self, n: int) -> int:
        dp = [math.inf] * (n+1)
        dp[0] = 0

        for i in range(1, n+1):
            for num in range(i+1):
                if (i - num*num) >= 0:
                    dp[i] = min(dp[i-num*num]+1, dp[i])
        return dp[n]