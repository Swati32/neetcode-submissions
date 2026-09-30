class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s or len(s) < len(t):
            return ""

        target = {}
        for ch in t: 
            target[ch] = target.get(ch,0) + 1
        
        window = {}
        min_len, min_window = math.inf,[-1, -1]
        have, need = 0, len(target)
        L = 0

        for R in range(len(s)):
            ch = s[R]
            window[ch] = window.get(ch, 0) + 1 
            if ch in target and window[ch] == target[ch]:
                have += 1
            
            while have == need:
                if min_len > R-L+1:
                    min_len = R-L+1
                    min_window = [L, R]

                ch = s[L]
                window[ch] -= 1
                if ch in target and window[ch] < target[ch]:
                    have -= 1
                L+= 1
            
        L, R = min_window
        return s[L : R+ 1] if min_len != math.inf else ""


            

                