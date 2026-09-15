# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode | None) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        ans = []

        def preorder(node):
            if node is not None:
                ans.append(node)
                preorder(node.left)
                preorder(node.right)

        preorder(root)

        for i in range(len(ans)):
            ans[i].left = None

            if i + 1 < len(ans):
                ans[i].right = ans[i + 1]
