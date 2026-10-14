class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        m = len(coins)
        n = amount
        dp = [[math.inf] * (n+1) for _ in range(m+1)]
        
        for i in range(m+1):
            dp[i][0] = 0
        
        for i in range(1,m+1):
            val = coins[i-1]
            for j in range(1,n+1):
                if j-val >= 0:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-val]+1)
                else:
                    dp[i][j] = dp[i-1][j]
        
        return dp[m][n] if dp[m][n]!= math.inf else -1

'''
Amount (j) --------->
               0        1        2        3        4        5
            +--------+--------+--------+--------+--------+--------+
Row 0: None |   0    |  inf   |  inf   |  inf   |  inf   |  inf   |  <-- Base Row (0 coins)
            +--------+--------+--------+--------+--------+--------+
Row 1: [1]  |   0    |   1    |   2    |   3    |   4    |   5    |
            +--------+--------+--------+--------+--------+--------+
Row 2: [2]  |   0    |   1    |   1    |   2    |   2    |   3    |
            +--------+--------+--------+--------+--------+--------+
Row 3: [5]  |   0    |   1    |   1    |   2    |   2    |   1    |  <-- Ans: dp[3][5] = 1
            +--------+--------+--------+--------+--------+--------+
                ^
            Base Col (Amount 0)
'''
