class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        window = [0] * 26
        required = [0] * 26

        for char in s1:
            required[ord(char) - ord("a")] +=1# 0-index var.  a - a = 0

        left = 0
        for right in range(len(s2)):
            
            window[ord(s2[right]) - ord("a")] += 1 

            if right - left + 1 > len(s1):
                window[ord(s2[left]) - ord("a")] -= 1
                left += 1

            if right - left + 1 == len(s1):
                if window == required:
                    return True

        return False