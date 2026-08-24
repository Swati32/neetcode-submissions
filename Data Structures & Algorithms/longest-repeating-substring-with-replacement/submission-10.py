class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        L = 0
        max_len = 0
        result = 0

        for R in range(len(s)):
            count[s[R]] = count.get(s[R], 0) + 1
            max_len = max(max_len, count[s[R]])

            while (R-L+1) - max_len > k:
                count[s[L]] = count[s[L]] - 1
                L += 1
            
            result = max(max_len, R-L+1)
        
        return result

                
