class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        longest = ""
        if n == 1:
            return s
        
        dp = [[False] * n for i in range(n)]

        for length in range(1, n+1):
            for start in range(n-length+1):
                end = start + length - 1
                # substrign = s[start: end + 1]

                if length <= 2:
                    dp[start][end] = s[start] == s[end]
                else:
                    dp[start][end] = s[start] == s[end] and (dp[start+1][end-1])
                
                if dp[start][end]:
                    if len(s[start:end+1]) > len(longest):
                        longest = s[start:end+1]
        

        return longest

                

        
            