class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}                            # 1. State: frequency map of chars in window
        L = 0                                 # 2. Left pointer boundary
        max_len = 0                           # 3. Count of the most frequent single character in window
        result = 0                            # 4. Global longest valid substring length found

        for R in range(len(s)):               # 5. Right pointer expands the window
            count[s[R]] = count.get(s[R], 0) + 1  # 6. Step 1 (Expand): increment incoming char count
            max_len = max(max_len, count[s[R]])   # 7. Update highest frequency character seen so far

            while (R - L + 1) - max_len > k:  # 8. Step 2 (Shrink): check if needed replacements > k
                count[s[L]] = count[s[L]] - 1 # 9. Decrement outgoing leftmost char
                L += 1                        # 10. Advance left pointer

            result = max(result, R - L + 1)   # 11. Step 3 (Process): window is valid, update max length

        return result                         # 12. Return the best length