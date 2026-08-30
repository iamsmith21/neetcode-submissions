class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        rows, cols = len(heights) , len(heights[0])
        #top and left r and c == 0 
        def canReachPacific(r,c, visited):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False

            if (r,c) in visited:
                return False

            if r == 0 or c == 0 :
                return True

            visited.add((r,c))

            # heights[r][c]
            for dr, dc in [(-1,0), (1,0), (0,1), (0,-1)]:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < rows and 0 <= nc < cols and heights[nr][nc] <= heights[r][c]:
                    if canReachPacific(nr,nc, visited):
                        return True
            return False

        
        def canReachAtlantic(r,c, visited):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False

            if (r,c) in visited:
                return False

            if r == rows -1  or c == cols -1 :
                return True

            visited.add((r,c))

            # heights[r][c]
            for dr, dc in [(-1,0), (1,0), (0,1), (0,-1)]:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < rows and 0 <= nc < cols and heights[nr][nc] <= heights[r][c]:
                    if canReachAtlantic(nr,nc, visited):
                        return True
            return False

        res = []
        for i in range(rows):
            for j in range(cols):
                visited1 = set()
                visited2 = set()
                if canReachAtlantic(i,j, visited1) and canReachPacific(i, j, visited2):
                    res.append([i,j])
        
        return res



            