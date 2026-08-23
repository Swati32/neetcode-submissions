class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        max_length = 0
        L = 0

        for R in range(len(s)):
            if s[R] in seen:
                while s[R] in seen:
                    seen.remove(s[L])
                    L += 1
                          
            seen.add(s[R])
            length = R - L + 1
            max_length = max(length, max_length)

        return max_length

            