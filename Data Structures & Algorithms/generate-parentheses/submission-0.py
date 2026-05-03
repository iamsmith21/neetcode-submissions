class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        
        def backTrack(s="", open=0,close=0):
            if len(s) == 2 * n:
                result.append(s)
                return 
            
            if open < n:
                backTrack(s+"(", open +1, close)
            if close < open:
                backTrack(s+")",open,close+1)
        
        backTrack()
        return (result)