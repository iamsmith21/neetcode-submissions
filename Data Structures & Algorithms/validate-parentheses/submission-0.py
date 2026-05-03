class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = { "}":"{",
                "]":"[",
                ")":"("
            }

        for c in s:
            if c in d:
                if len(stack)!=0 and stack[-1] == d[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        if len(stack) == 0:
            return True
        else:
            return False
            
        