class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        max_len = [0]
        start = [0]

        def check_palindrome(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > max_len[0]:
                    max_len[0] = r-l+1
                    start[0] = l
                l -= 1
                r += 1
            return (start, max_len)

        for i in range(len(s)):
            check_palindrome(i, i)
            if i+1 < len(s):
                check_palindrome(i, i+1)
                
        return s[start[0]: start[0] + max_len[0]]