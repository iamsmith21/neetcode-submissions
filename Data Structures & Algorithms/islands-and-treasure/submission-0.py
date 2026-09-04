class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c, 0))

        while q:
            r, c, dist = q.popleft()
            neighbours = [(0,1), (0,-1), (1,0), (-1,0)]

            for nr, nc in neighbours:
                cr, cc = nr + r, nc + c

                if cr >= 0 and cr < rows and cc >= 0 and cc < cols and grid[cr][cc] == 2147483647:
                    grid[cr][cc] = dist + 1
                    q.append((cr,cc, dist + 1))

        



        
