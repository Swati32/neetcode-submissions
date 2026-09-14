class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = { ')':'(','}': '{', ']': '['}

        for ch in s :
            if ch in ('(', '[' ,'{'):
                stack.append(ch)
            elif ch in match.keys() and stack and stack[-1] == match[ch]:
                stack.pop()
            else:
                return False

        return not stack
