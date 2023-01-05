class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buy = prices[0]
        max_profit = 0
        for price in prices:
            if (buy > price):
                buy = price
            
            profit = price - buy
            if (profit > max_profit):
                max_profit = profit
        return max_profit;