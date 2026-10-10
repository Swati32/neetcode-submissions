class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices:
            return 0

        holding = -prices[0]  # Buying on day 0 costs prices[0]
        sold = 0
        cooldown = 0

        for price in prices[1:]:
            prev_sold = sold

            # Sell today: realize profit from held stock
            sold = holding + price

            # Hold today: keep held stock OR buy fresh from cooldown cash
            holding = max(holding, cooldown - price)

            # Rest today: best non-stock balance between yesterday's rest or sale
            cooldown = max(cooldown, prev_sold)

        return max(sold, cooldown)