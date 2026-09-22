class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []

        stack.append(0)
        res = [0] * len(temperatures)


        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                curr_index = stack.pop()
                res[curr_index] = i - curr_index 
            
            stack.append(i)
               
            
        return res