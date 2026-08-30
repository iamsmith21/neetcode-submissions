class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        if numRows == 0:
            return []

        

        triangle = [[1]]
      
        for i in range(1,numRows):
            previous = triangle[i-1] 
            res = [1]

            for j in range(len(previous) - 1):
                res.append(previous[j] + previous[j+1])
            
            res.append(1)
            triangle.append(res)

        return triangle

            

            
          
