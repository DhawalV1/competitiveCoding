# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        
        def dfs(root):
            if not root:
                return None
        
        
            lt = dfs(root.left)
            rt = dfs(root.right)
            
            if lt:
                lt.right = root.right
                root.right = root.left
                root.left = None
                
            return rt or lt or root
        
        return dfs(root)
        
        
        
        
        
        
        
        
        
        
        curr = root
        
        while curr:
            if curr.left != None:
                p = curr.left
                while p.right != None:
                    p = p.right
                    
                p.right = curr.right
                
                curr.right = curr.left
                curr.left = None
            
            curr = curr.right
        
      
        