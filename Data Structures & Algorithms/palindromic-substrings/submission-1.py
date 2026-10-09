class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0

        count = 0
        
        def count_palindrome(l, r):
            cnt = 0
            while l >=0 and r < len(s) and s[l] == s[r]:
                cnt += 1
                l -= 1
                r += 1
            return cnt
        
        for i in range(len(s)):
            count += count_palindrome(i, i)
            count += count_palindrome(i, i+1)
        
        return count 


        