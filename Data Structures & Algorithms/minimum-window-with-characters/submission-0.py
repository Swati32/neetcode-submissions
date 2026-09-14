class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s or len(s) < len(t):
            return ""

        target = {}
        for ch in t: 
            target[ch] = target.get(ch,0) + 1
        
        min_len = math.inf
        start_idx = 0
        window ={}
        have, need = 0, len(target)
        l = 0

        for r in range(len(s)):
            ch = s[r]
            window[ch] = window.get(ch, 0) + 1

            if ch in target and window[ch] == target[ch]:
                have += 1

            while have == need:
                cur_len = r - l + 1
                if cur_len < min_len:
                    min_len = cur_len
                    start_idx = l

                lch = s[l]
                window[lch] -= 1
                if lch in target and window[lch] < target[lch]:
                    have -=1
                l+=1
            
        return s[start_idx : start_idx + min_len] if min_len != float("inf") else ""


            
            


