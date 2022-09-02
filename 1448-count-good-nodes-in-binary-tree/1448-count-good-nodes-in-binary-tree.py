# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.gd(root,-10000)
    
    def gd(self,root,ma):
        if root is None:
            return 0
        if ma <= root.val:
            res = 1
        else: res = 0
            
        res += self.gd(root.left,max(root.val,ma))
        res += self.gd(root.right,max(root.val,ma))
        
        return res
        
        
        
        
        
        