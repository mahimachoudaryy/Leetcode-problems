# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        q = deque([root])
        ans = []
        l = 0
        
        while len(q) > 0:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
                level.append(node.val)
            if l % 2 == 1:
                ans.append(level[::-1])
            else:
                ans.append(level)

            l += 1   
        
        return ans
