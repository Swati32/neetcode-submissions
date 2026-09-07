class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        def expand_around_center(l, r):
            i, j = l, r
            while i >= 0 and j<len(s) and s[i] == s[j]:
                i = i-1
                j = j+1
            return s[i+1:j]

        for i in range(len(s)):
          s1 = expand_around_center(i, i)
          s2 = expand_around_center(i,i+1)

          if len(s1) >= len(res):
            res = s1
          if len(s2) >= len(res):
            res = s2
          
        return res
