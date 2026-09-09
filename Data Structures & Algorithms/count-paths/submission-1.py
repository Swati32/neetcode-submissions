class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)] 
        dp[0][0] = 1

        def value(r,c):
            if 0<=r<m and 0<=c<n:
                return dp[r][c]
            return 0

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                dp[i][j] = value(i-1, j) + value(i, j-1)


        return dp[m-1][n-1]


