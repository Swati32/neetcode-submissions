class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0

        prev1, prev2 = 1, 1

        for i in range(1, len(s)):
            total_ways = 0

            if s[i] != "0":
                total_ways += prev1
            
            if "10" <= s[i-1:i+1] <= "26":
                total_ways += prev2

            if total_ways == 0:
                return 0
            
            prev2, prev1 = prev1, total_ways
    
        return prev1
            
        