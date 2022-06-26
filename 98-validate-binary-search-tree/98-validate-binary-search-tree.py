# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        inf = sys.maxsize
        
        return self.helper(root,-inf,inf)
    
    def helper(self, root, lower,higher):
        
        if root is None:
            return True
        
        if lower < root.val < higher:
            return self.helper(root.left,lower,root.val) and self.helper(root.right,root.val,higher)
        
        else:
            return False
        
        
        