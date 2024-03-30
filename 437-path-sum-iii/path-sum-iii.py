# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    #global ans 
    ans =0
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        if not root: return 0
        
        self.helper(root,targetSum)
        self.pathSum(root.left,targetSum)
        self.pathSum(root.right,targetSum)
        
        return self.ans
        
    
    
    def helper(self, root: Optional[TreeNode], sm: int):
        
        
        if not root : return
        
        if root.val == sm : self.ans+=1
        
        self.helper(root.left,sm-root.val)
        self.helper(root.right,sm-root.val)
        