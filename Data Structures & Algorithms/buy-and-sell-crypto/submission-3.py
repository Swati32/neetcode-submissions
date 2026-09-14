class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0
        max_profit = 0
        
        for R in range(1, len(prices)):
            if prices[L] > prices[R]:
                L = R
            else:
                profit = prices[R] - prices[L]
                max_profit= max(max_profit, profit)
        
        return max_profit
            
            