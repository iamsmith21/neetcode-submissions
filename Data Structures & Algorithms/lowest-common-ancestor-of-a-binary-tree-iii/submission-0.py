"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        ancestors = set()

        node = p
        while node:
            ancestors.add(node)
            node = node.parent

        while q:
            if q in ancestors:
                return q 
            q = q.parent