class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        seen = Counter(s)
        
        for ch in t:
            if ch not in seen:
                return False
            seen[ch] -= 1
        
        for k in seen.values():
            if k != 0:
                return False
        
        return True