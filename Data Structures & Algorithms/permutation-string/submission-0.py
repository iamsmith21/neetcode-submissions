from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        d1 = Counter(s1)
        window_size = len(s1)

        for i in range(len(s2)):
            subStr = s2[i : window_size + i]

            d2 = Counter(subStr)

            if d1 == d2:
                return True
        
        return False
