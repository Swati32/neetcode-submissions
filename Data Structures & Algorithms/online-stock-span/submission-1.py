class StockSpanner:
    def __init__(self):
        # Monotonic decreasing stack storing (price, accumulated_span)
        self.stack = []

    '''
    for stack top (num, n)
    we know there are n elements smaller than num. so if a greater number comes along span of 2  
    represents all the numbers smaller than 2 and we add the span. We keep doing this over and over
    till stack top num < incoming num 
    '''
    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            prev_price, prev_span = self.stack.pop()
            span += prev_span

        self.stack.append((price, span))
        return span