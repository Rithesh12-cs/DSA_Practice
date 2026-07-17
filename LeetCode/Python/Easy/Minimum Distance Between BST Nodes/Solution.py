# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        listt=[]
        def inOrder(node):
            if node is None:
                return
            inOrder(node.left)
            listt.append(node.val)
            inOrder(node.right)

        inOrder(root)
        difff=float('inf')
        for i in range(1,len(listt)):
            diff=(listt[i] - listt[i-1])
            difff=min(difff,diff)
        return difff
        