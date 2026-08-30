class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i , j = 0, 0 

        while j < len(s) and i < len(t):
            if s[j] == t[i]:
                j += 1
                i += 1
                continue
            j += 1
        
        return len(t) - i