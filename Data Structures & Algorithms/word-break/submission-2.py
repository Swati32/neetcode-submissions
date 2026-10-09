class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True

        for i in range(1, n+1):
            for word in wordDict:
                k = len(word)
                if i - k >= 0 and dp[i-k] and s[i-k:i] == word:
                    dp[i] = True
                    break
        
        return dp[n]
