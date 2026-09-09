class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n= len(text1), len(text2)
        dp = [[0] * n for _ in range(m)]

        def value(r,c):
            if 0 <= r < m and 0 <= c < n:
                return dp[r][c]
            return 0

        for i in range(m):
            for j in range(n):
                if text1[i] == text2[j]:
                    dp[i][j] = value(i-1,j-1) + 1
                else:
                    dp[i][j] = max(value(i-1,j), value(i, j-1))

        return dp[m-1][n-1]    