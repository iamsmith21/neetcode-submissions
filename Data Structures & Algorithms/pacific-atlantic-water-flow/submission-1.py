class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        rows, cols = len(heights), len(heights[0])
        def dfs(r,c, visited):
            if r < 0 or r >= rows or c < 0 or c>= cols:
                return
            
            if (r,c) in visited:
                return

            visited.add((r,c))

            for dr , dc in [(-1,0), (1,0), (0,1), (0,-1)]:
                nr = r + dr
                nc = c + dc

                if nr >= 0 and nr < rows and nc >= 0 and nc < cols and heights[nr][nc] >= heights[r][c]:
                    dfs(nr,nc, visited)

        
        pacific = set()
        atlantic = set()


        for c in range(cols):
           dfs(0,c, pacific)

        for r in range(rows):
            dfs(r,0, pacific) 

        for c in range(cols):
            dfs(rows - 1, c, atlantic)

        for r in range(rows):
            dfs(r, cols -1, atlantic)
        
        res = []
        for r,c in pacific & atlantic:
            res.append([r,c])

        return res