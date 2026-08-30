class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict1 = {}

        for char in s:
            dict1[char] = dict1.get(char, 0) + 1

        for k, v in dict1.items():
            if v == 1:
                return s.index(k)
        
        return -1

        