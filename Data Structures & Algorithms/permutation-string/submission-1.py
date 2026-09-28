from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        d1 = Counter(s1)
        window_size = len(s1)

        freq = {}
        left = 0

        for right in range(len(s2)):
            incoming = s2[right]
            freq[incoming] = freq.get(incoming, 0) + 1

            if right - left + 1 > window_size:
                outgoing = s2[left]
                freq[outgoing] -= 1

                if freq[outgoing] == 0:
                    del freq[outgoing]
                
                left += 1

            if right - left + 1 == window_size:
                if freq == d1:
                    return True
        
        return False
