class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        q = deque([(0, -1)])
        # (node, parent)
        dict1 = {i : [] for i in range(n)}
        visited= set()

        for k, v in edges:
            dict1[k].append(v)
            dict1[v].append(k)

        while q:
            node, parent = q.popleft()

            for nei in dict1[node]:
                if nei not in visited:
                    q.append((nei, node))
            visited.add(node)

            if len(visited) == n and len(q) != 0:
                return False

        return len(visited) == n
