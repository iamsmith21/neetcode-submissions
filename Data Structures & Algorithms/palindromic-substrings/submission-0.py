class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        n = len(s)

        dp = [[False] * n for i in range(n)]

        for length in range(1, n+1):
            for start in range(n-length+1):
                # for length = 2 and n = 3 
                # start = 0 1 
                end = start + length - 1

                if length <= 2:
                    dp[start][end] = s[start] == s[end]
                else:
                    dp[start][end] = (s[start] == s[end]) and (dp[start+1][end-1])
                
                if dp[start][end]:
                    count += 1
        
        return count