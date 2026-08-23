class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0
        max_profit = 0
        
        for R in range(len(prices)):
            profit = prices[R] - prices[L]
            max_profit = max(max_profit, profit)

            if prices[L] >= prices[R]:
                L = R
            else:
                R += 1
    
        return max_profit