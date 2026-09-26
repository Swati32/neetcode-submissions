class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        running_min = math.inf
        max_profit = 0
        for price in prices:
            if price < running_min:
                running_min = price
            else:
                profit = price - running_min
                max_profit += profit
                running_min = price
        return max_profit

        