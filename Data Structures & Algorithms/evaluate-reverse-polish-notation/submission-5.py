class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token not in ('+','-','*','/'):
                stack.append(int(token))
            else:
                num1 = stack.pop()
                num2 = stack.pop()

                if token == '+':
                    stack.append(num1+num2)
                elif token == '-':
                    stack.append(num2-num1)
                elif token == '*':
                    stack.append(num2*num1)
                else:
                    stack.append(int(num2/num1))
        
        return stack[-1] if stack else None

        