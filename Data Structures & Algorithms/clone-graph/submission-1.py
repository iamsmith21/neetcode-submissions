"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        dict1 = {}

        def dfs(cur):
            if not cur:
                return None

            if cur in dict1:
                return dict1[cur]

            copy = Node(cur.val)
            dict1[cur] = copy

            for neighbor in cur.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy
        
        return dfs(node)