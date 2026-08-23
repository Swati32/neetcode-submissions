class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seen = {}
        for letter in s:
            if letter in seen:
                seen[letter] += 1
            else:
                seen[letter] = 1
        
        for letter in t:
            if letter not in seen:
                return False
            seen[letter] -= 1
            if seen[letter] < 0:
                return False
        
        for key, value in seen.items():
            if value != 0:
                return False
            
        return True
