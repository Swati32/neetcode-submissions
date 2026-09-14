class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        if k > len(s2):
            return False
        
        s1_count = {}
        for ch in s1:
            s1_count[ch] = s1_count.get(ch, 0) + 1

        window = {}
        L= 0

        for R in range(len(s2)):
            window[s2[R]] = window.get(s2[R], 0) + 1

           
            if R-L+1 > k:
                window[s2[L]] -= 1
                if window[s2[L]] == 0:
                    del window[s2[L]]
                L+=1

            if R-L+1 == k and window == s1_count:
                return True 

    
        return False




        