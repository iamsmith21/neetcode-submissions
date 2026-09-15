class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        if n <= 1:
            return n

        dict1 = {i : [] for i in range(n)}
        for i, j in edges:
            dict1[i].append(j)
            dict1[j].append(i)

        # {0: [1], 1: [0, 2], 2: [1], 3: [4], 4: [3]}
        visited = set()
        q = deque()

        def findCount(q, count):
            while q:
                value = q.popleft()

                for v in dict1[value]:
                    if v not in visited:
                        q.append(v)
                
                visited.add(value)
                
            if not q:
                count += 1
            return count

                    

        count = 0

        for i in range(n):
            if i not in visited:
                q.append(i)
                count = findCount(q, count)

        return count