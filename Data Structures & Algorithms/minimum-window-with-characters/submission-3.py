class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tmap = Counter(t)

        L = 0
        smap = defaultdict(int)
        min_len = math.inf
        start = 0
        need = len(tmap)
        have = 0

        for R in range(len(s)):
            smap[s[R]] += 1
            if smap[s[R]] == tmap[s[R]]:
                have += 1
            
            while have == need and L < len(s):
                if (R - L + 1) < min_len:
                    min_len = R-L+1
                    start = L
                if s[L] in tmap and smap[s[L]] == tmap[s[L]]:
                    have -= 1
                smap[s[L]] -= 1
                L += 1
        
        return s[start: start + min_len] if min_len != math.inf else ""
