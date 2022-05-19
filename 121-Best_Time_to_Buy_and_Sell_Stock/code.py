# RUN TIME ERROR CODE 1
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        for i in range(n-1):
            next_stock = prices[i+1:n]
            max_price = max(next_stock)
            cur_profit = max(next_stock) - prices[i]
            if cur_profit > 0 and cur_profit > max_profit:
                max_profit = cur_profit
        return max_profit

# RUN TIME ERRROR CODE 2
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = 10^5
        for price in prices:
            min_price = min(price, min_price)
            max_profit = max(max_profit, price - min_price)

        return max_profit

# PASS CODE
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = 10^5

        cur_day = 0
        next_day = 1

        while next_day < len(prices):
            if prices[cur_day] < prices[next_day]:
                profit = prices[next_day] - prices[cur_day]
                max_profit = max(profit, max_profit)
            else:
                cur_day = next_day
            next_day += 1
        return max_profit

# USE TWO POINTER + CHANGE CURRENT ONLY WHEN NEXT PRICE IS LESS OR EQUAL TO CURRENT PRICE

