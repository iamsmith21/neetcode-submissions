class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        dp = [[0,0] for _ in range(n +2)]

        for day in range(n - 1, -1 , -1):
            skip = dp[day + 1][0]
            buy = -prices[day] + dp[day + 1][1]

            hold = dp[day + 1][1]
            sell = prices[day] + dp[day + 2][0]
            
            dp[day][1] = max(hold, sell)
            dp[day][0] = max(skip, buy)

        return dp[0][0]