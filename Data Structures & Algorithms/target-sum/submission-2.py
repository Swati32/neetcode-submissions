class Solution:
    def findTargetSumWays(self, nums: list[int], t: int) -> int:
        total = sum(nums)
        if total < abs(t) or (total + t) % 2 != 0:
            return 0
    
        '''
        Every number goes into either $P$ or $N$, so $P + N = \text{total}$, and we want $P - N = t$.Adding those two equations cancels $N$: $2P = \text{total} + t \implies P = (\text{total} + t) // 2$. So instead of guessing signs, you just count how many subsets sum to target ($P$).
        '''
        target = (total + t) // 2
        n = target
        m = len(nums)
    
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = 1

        for i in range(1, m + 1):
            val = nums[i - 1]
            for j in range(n + 1):
                if j >= val:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - val]
                else:
                    dp[i][j] = dp[i-1][j]
                
        return dp[m][n]

'''
+---------------------------------------+
                     |         Knapsack Decision Tree        |
                     +---------------------------------------+
                                        |
                 +----------------------+----------------------+
                 |                                             |
        Item Reuse Policy?                             What is the Goal?
        /                \                             /       |       \
   Single-Use         Infinite Reuse              Feasibility  Count   Optimize
   (0/1 Knapsack)    (Unbounded Knapsack)          (or / bool)  (+)     (min / max)
        |                     |                        |        |        |
  • Target Sum          • Coin Change 1                |        |        |
  • Partition Subset                                   |        |        |
                                             Partition Subset  Target   Coin
                                                    Sum         Sum    Change 1
'''