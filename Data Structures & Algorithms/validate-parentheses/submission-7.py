class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hmap = {')':'(', '}':'{', ']':'['}
        if (len(s)%2 != 0):
            return False

        for i in range(len(s)):
            if s[i] in hmap.values():
                stack.append(s[i])
            elif s[i] in hmap:
                if not stack or hmap[s[i]] != stack[-1]:
                    return False
                stack.pop()
        
        return len(stack) == 0
        