class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Bounded Knapsack
        # Either Check if sum $j$ is achievable without item $i$ (Skip), or if remaining sum $j - \text{val}$ was achieved using prior items (Take). Reading row i - 1 strictly enforces single-use.
        total = sum(nums)
        if total%2 != 0:
            return False
        target = total//2


        m = len(nums)
        n = target
        dp = [[False] * (n+1) for _ in range(m+1)]
        
        for i in range(m+1):
            dp[i][0] = True

        for i in range(1, m+1):
            val = nums[i-1]
            for j in range(1, n+1):
                if j-val >= 0:
                    dp[i][j] = dp[i-1][j-val] or dp[i-1][j]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[m][n]


'''
Option 1: Take the 3 (dp[i - 1][j - val]): If you put 3 in your bag, you still need 7 - 3 = 4 more. So you look up at the previous row (i - 1, before 3 was available) at column 4 to check if the earlier numbers could already make 4.

Option 2: Skip the 3 (dp[i - 1][j]): If you ignore 3, you still need the full 7. So you look straight up at dp[i - 1][7] to see if the earlier numbers could already make 7 on their own.
'''

                
        