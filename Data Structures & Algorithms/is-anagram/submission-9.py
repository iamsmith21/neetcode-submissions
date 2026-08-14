class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        
        charMap = {}

        for i in range(len(s)):
            charMap[s[i]] =  charMap.get(s[i], 0) + 1
        
        for j in t:
            if j in charMap.keys():
                charMap[j] = charMap[j] - 1
            
        for value in charMap.values():
            if value != 0:
                return False
        
        return True

        # charMap1 = {} 
        # charMap2 = {} 

        # for i, char in enumerate(s):
        #     charMap1[char] = charMap1.get(char, 0) + 1

        # for i, char in enumerate(t):
        #     charMap2[char] = charMap2.get(char, 0) + 1
        
        # return charMap1 == charMap2
