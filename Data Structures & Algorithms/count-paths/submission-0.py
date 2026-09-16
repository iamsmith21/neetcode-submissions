class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        rows = [1] * n # [1,1,1]

        #we are marking last row and last col = 1

        for i in range(m - 1):
            newRow = [1] * n

            for j in range(n-2, -1, -1):
                newRow[j] = newRow[j + 1] + rows[j]
            rows = newRow
        
        return rows[0]
