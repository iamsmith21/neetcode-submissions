class Solution:
    def maxDifference(self, s: str) -> int:
        dict1 = {}

        diff = 0
        # if odd diff ++ 
        # if even diff -- 
        for i in s:
            dict1[i] = dict1.get(i,0) + 1
        
        odd = 0
        even = 1000
        for values in dict1.values():
            if values%2 != 0 and values > odd:
                odd= values
            elif values%2 == 0 and values < even:
                even = values
        
        return odd - even
               
            

        