class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        Okay, so from what i understand. we always check whats max_len that is most frequently occuring character. if the window size - most frequent occurence in past or present, we exceed L by 1 cause we know that in current window we have already expired our budget so cant go beyond it. So we increment l till we get our budget back so we can find a better window down the line if possible.
        '''
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
            
            result = max(result, R-L+1)
        
        return result

                
