class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        total = 0
        stack = []
        oper = ["+", "-", "*", "/"]

        if len(tokens) == 1:
            return int(tokens[0])
        for i in tokens:
            if i not in oper:
                stack.append(i) # 1 2
            else:
                if len(stack) >= 2:
                    var2 = stack.pop()
                    var1 = stack.pop()
                    total = int(eval(f"{var1}{i}{var2}"))
                    stack.append(total)
        
        return total