class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        window = 0  
        max_profit = 0
        while window < len(prices):
            i = 0
            while i < len(prices) - window :
                profit = prices[i+window] - prices[i]
                max_profit = max(max_profit, profit)
                i += 1
            window += 1

        return max_profit