class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        m, n = len(coins), amount
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(m + 1):
            dp[i][0] = 1  # 0 amount banane ka exact 1 tareeqa

        for i in range(1, m + 1):
            val = coins[i - 1]
            for j in range(1, n + 1):
                if j >= val:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - val]  # Skip + Take (same row)
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[m][n]