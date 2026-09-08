class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n+1)

        word_set = set()
        for word in wordDict:
            word_set.add(word)

        dp[0]= True
        

        for i in range(1, n+1):
            for j in range(i, -1, -1):
                dp[i] = dp[j] and s[j:i] in word_set 
                if dp[i]:
                    break
        
        return dp[n]

        