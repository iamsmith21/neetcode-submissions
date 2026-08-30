# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        result = []

        queue = deque([root])

        switch = True
        while queue:
            level_size = len(queue)
            curr_level = []

            for _ in range(level_size):
                node = queue.popleft()
                curr_level.append(node.val)

                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if switch:
                result.append(curr_level)
                switch = not switch
            else:
                result.append(curr_level[::-1])
                switch = not switch


        return result