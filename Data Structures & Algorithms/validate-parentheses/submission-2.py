class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = { ")" : "(", "]" : "[", "}" : "{" }

        for chr in s:
            if chr in ['(', '[','{']:
                stack.append(chr)
            else:
                if chr in match.keys() and stack and stack[-1] == match[chr]:
                    stack.pop()   
                else:
                    return False
        return not stack