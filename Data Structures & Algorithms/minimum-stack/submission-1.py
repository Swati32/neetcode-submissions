class MinStack:

    def __init__(self):
        self.stack = []        

    def push(self, val: int) -> None:
        if self.stack:
            current_min = min(val, self.stack[-1][1])
            self.stack.append((val, current_min))
        else:
            self.stack.append((val, val))
        

    def pop(self) -> None:
        if self.stack:
            popped = self.stack.pop()
            return popped[0]

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]
        
    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]
