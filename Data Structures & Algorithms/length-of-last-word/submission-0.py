class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr = s.split()
        
        for i in arr:
            if i == " ":
                arr.remove(i)
        
        return len(arr[-1])