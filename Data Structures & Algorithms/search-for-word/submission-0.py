class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        visited = set()

        def dfs(r, c, index):

            if index == len(word):
                return True
            
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False

            if (r,c) in visited:
                return False
            
            if board[r][c] != word[index]:
                return False
            
            visited.add((r,c))
            found = False
            for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                nr, nc = r + dr, c + dc
                if dfs(nr, nc, index + 1):
                    found = True
                    break

            visited.remove((r,c))

            return found
        

        for i in range(rows):
            for j in range(cols):
                if dfs(i , j , 0):
                    return True
        
        return False

