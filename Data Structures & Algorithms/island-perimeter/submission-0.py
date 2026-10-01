class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid) , len(grid[0])
        
        # globalSum = 0
        def dfs(r, c):
            if (r < 0 or r >= rows or c < 0 or c >= cols):
                return 1
            
            if (r,c) in visited:
                return 0

            if grid[r][c] == 0:
                return 1

            visited.add((r,c))

            perimeter = 0
            for nr, nc in [(0,1), (0,-1), (1,0), (-1,0)]:
                cr , cc = nr + r, nc + c
                perimeter += dfs(cr, cc)

            return perimeter
            

            

        visited = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return dfs(r, c)
                    break
        
  
