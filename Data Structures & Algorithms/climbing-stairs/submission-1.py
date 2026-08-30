class Solution:
    def climbStairs(self, n: int) -> int:
        # n = 2 , 1+1 , 2 2 ways

        dp = [0]*(n+1)

        if n == 1:
            return 1
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[-1]