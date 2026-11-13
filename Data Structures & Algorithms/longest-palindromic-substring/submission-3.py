class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        self.max_len = 0
        self.start = 0

        def check_palindrome(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > self.max_len:
                    self.max_len = r-l+1
                    self.start = l
                l -= 1
                r += 1

        for i in range(len(s)):
            check_palindrome(i, i)
            check_palindrome(i, i+1)
                
        return s[self.start: self.start + self.max_len]