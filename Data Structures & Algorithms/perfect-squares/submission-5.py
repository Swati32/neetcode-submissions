class Solution:
    def numSquares(self, n: int) -> int:
        dp = [math.inf] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            for num in range(1, int(i**0.5) + 1):
                square = num * num
                dp[i] = min(dp[i], dp[i - square] + 1)

        return dp[n]