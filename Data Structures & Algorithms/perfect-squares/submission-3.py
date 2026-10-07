class Solution:
    def numSquares(self, n: int) -> int:
        if n == 1:
            return 1
        dp = [math.inf] * (n+1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n+1):
            for num in range(i):
                if (i - num*num) >= 0:
                    dp[i] = min(dp[i-num*num]+1, dp[i])
        return dp[n]