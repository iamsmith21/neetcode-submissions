class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(r,c, visited):
            if r >= rows or r < 0 or c >= cols or c < 0:
                return 0

            if (r,c) in visited:
                return 0

            if grid[r][c] == 0:
                return 0
            
            visited.add((r,c))
            area = 1
            dirn = [(0,1),(0,-1), (1,0), (-1,0)]
            for nr, nc in dirn:
                cr, cc = r + nr, c + nc
                area += dfs(cr,cc,visited)

            return area




        globalArea = 0
        visited = set()
        for r in range(rows):
            for c in range(cols):
                area = dfs(r,c,visited)
                globalArea = max(area, globalArea)
                   
        return globalArea

     
            