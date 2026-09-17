class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        memo = {}

        def solve(day, holding):

            if day >= len(prices):
                return 0

            if (day, holding) in memo:
                return memo[(day, holding)]

            if holding:
                skip = solve(day + 1, True)
                sell = prices[day] + solve(day + 2, False)

                memo[(day, holding)] = max(skip, sell)
                return memo[(day, holding)]
            else:
                skip = solve(day + 1, False)
                buy = -prices[day] + solve(day + 1, True)
                memo[(day, holding)] = max(skip, buy)
                return memo[(day, holding)] 


        
        return solve( 0, False)