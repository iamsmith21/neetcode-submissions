class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        longest = ""
        st = 0
        en = 0
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
                    if end - start +1 > en - st:
                        st = start
                        en = end
        

        return s[st:en + 1]

                

        
            