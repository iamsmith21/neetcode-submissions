class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {} # {'a' : index}
        left = 0 
        right = 0
        longest = 0
        
        for i in range(len(s)):
            if s[i] in seen and seen[s[i]] >= left:
                    left = seen[s[i]] + 1
            seen[s[i]] = i
            longest = max(longest, right - left + 1)
            right += 1

        return longest