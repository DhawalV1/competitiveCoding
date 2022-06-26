# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        res = []
        
        
        self.helper(root,res,0)
        return res    
        
    def helper(self,root,res,depth):
        
        if root is None:
            return 
        
        if depth == len(res):
            res.append(root.val)
            
        self.helper(root.right,res,depth+1)
        self.helper(root.left,res,depth+1)
        