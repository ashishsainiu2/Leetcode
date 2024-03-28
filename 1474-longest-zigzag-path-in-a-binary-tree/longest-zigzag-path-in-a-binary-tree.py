# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #global mx 
    def __init__(self):
        self.mx=0
    
    def solve(self, root: Optional[TreeNode] , l, r):

        if not root:
            return

        self.mx = max(self.mx,l,r)

        self.solve(root.left, r+1,0)
        self.solve(root.right,0,l+1)

    
    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        self.solve(root,0,0)
        
        return self.mx