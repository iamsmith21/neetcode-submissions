class TrieNode:

    def __init__(self):
        self.children = {}
        self.isWord = False
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        rows, cols = len(board), len(board[0])
        visited = set()
        root = TrieNode()

        for word in words:
            node = root

            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                
                node = node.children[char]
            
            node.isWord = True
            node.word = word

        def dfs(r,c,node):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return

            if (r,c) in visited:
                return
            
            char = board[r][c]

            if char not in node.children:
                return 
            
            node = node.children[char]

            if node.isWord:
                res.append(node.word)
                node.isWord = None
            
            visited.add((r,c))

            for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                nr = r + dr
                nc = c + dc

                dfs(nr, nc, node)
            
            visited.remove((r,c))

        res = []
        for r in range(rows):
            for c in range(cols):
                dfs(r,c, root)
        
        return res
        