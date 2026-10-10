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
            for j in range(n+1):
                if j-val >= 0:
                    dp[i][j] = dp[i-1][j-val] or dp[i-1][j]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[m][n]



                
        