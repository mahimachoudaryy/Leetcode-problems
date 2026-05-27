# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:          
            return 0          
        q = deque([root]) 
        ans = [] 
        a=[]
        while(len(q)>0):
            level = [] 
            for i in range(len(q)):
                node = q.popleft() 
                if not node.left and not node.right:
                    return len(ans)+1
                if(node.left):
                    q.append(node.left) 
                if(node.right):
                    q.append(node.right) 
                level.append(node.val) 
            ans.append(level[-1])
            a.append(level[0])

        c = len(ans)
        b = len(a)

        return min(c, b)     
