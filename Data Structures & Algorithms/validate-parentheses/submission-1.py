class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for chr in s:
            if chr in ['(', '[','{']:
                stack.append(chr)
            else:
                if chr == ')' and stack and stack[-1] == '(':
                    stack.pop()   
                elif chr == ']' and stack and stack[-1] == '[':
                    stack.pop() 
                elif chr == '}' and stack and stack[-1] == '{':
                    stack.pop() 
                else:
                    return False
        return not stack