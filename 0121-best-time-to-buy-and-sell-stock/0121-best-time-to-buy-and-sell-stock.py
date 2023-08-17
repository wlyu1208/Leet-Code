class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer, n = 0, len(prices)
        buy = 10**4
        for i in range(n):
            today = prices[i]

            if today < buy:
                buy = today
            else:
                answer = max(answer, today - buy)
        
        return answer

