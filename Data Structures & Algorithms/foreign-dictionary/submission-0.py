class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        adj = {c : [] for w in words for c in w}

        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]

            
            minLen = min(len(w1), len(w2))


            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].append(w2[j])
                    break

            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
        
        visited = {}
        result = []

        def dfs(c):
            if c in visited:
                return not visited[c]
            
            visited[c] = False # now visiting but not fully explored
            for nei in adj[c]:
                if dfs(nei):
                    return True
            
            visited[c] = True
            result.append(c)
            return False
                
        for c in adj:
            if dfs(c):
                return ""
        result.reverse()

        return "".join(result)

