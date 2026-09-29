class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        str = strs[0]
        for i, ch in enumerate(str):
            for other_word in strs[1:]:
                if len(other_word) == i or other_word[i] != ch:
                    return other_word[:i]
        return str



        