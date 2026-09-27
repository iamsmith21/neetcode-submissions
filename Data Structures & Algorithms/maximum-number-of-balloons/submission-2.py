class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        myDict = {k : 0 for k in "balloon"}

        if len(text) < 7:
            return 0
        for c in text:
            if c in myDict:
                myDict[c] += 1
        
        lVal = myDict["l"] // 2
        oVal = myDict["o"] // 2

        return min(
            myDict["l"] // 2,
     myDict["o"] // 2,
     myDict["b"],
     myDict["a"],
     myDict["n"]
        )