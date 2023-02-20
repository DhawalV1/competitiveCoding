# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        
        def dfs(node,par,depth,val):
            
            if not node:
                return
            if node.val==val:return depth,par
            return dfs(node.left,node,depth+1,val) or dfs(node.right,node,depth+1,val)
        
        m,n = dfs(root,None,0,x)
        a,b = dfs(root,None,0,y)
        
        return m==a and n!=b 