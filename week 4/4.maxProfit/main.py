class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy = 0
        profit = 0
        for sell in range(1, len(prices)):
            diff = prices[sell] - prices[buy]
            if diff > profit:
                profit = diff
            elif diff < 0:
                buy = sell
        return profit

    def maxProfit2(self, prices: list[int]) -> int:
        max_profit = 0
        min_price = float('inf')

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit


s = Solution()
prices = [2, 1, 2, 1, 0, 1, 2]
print(s.maxProfit(prices))
