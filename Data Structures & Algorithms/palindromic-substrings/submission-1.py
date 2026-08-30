class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        globalCount = 0
        for i in range(n):
            count = 1

            # for odd length aba

            l = i - 1
            r = i + 1
            while l >= 0 and r < n:
                if s[l] == s[r]:
                    count += 1
                    l -= 1
                    r += 1
                else:
                    break

            # even length abba
        
            l = i
            r = i +1

            while l >= 0 and r < n:
                if s[l] == s[r]:
                    count += 1
                    l -= 1
                    r += 1
                else:
                    break
            
            globalCount += count

        return globalCount
